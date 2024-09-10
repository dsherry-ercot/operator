from pathlib import Path
import pandas as pd
from getpass import getuser
from datetime import datetime
import sys  #  Input and output files names are in sys.argv

# import re   #  Regular Expressions Parsing for patterns
# import numpy as np

USER_DIRECTORY = Path(f"C:/Users/{getuser()}")

version = "v1-5, 7/16/2024"

#  Program: ReadConvLog.py inputFile.log outputFile.xlsx
#  Author:  Vicki Scott
#  Date:    7/10/2024
#  Version History:  Current version is v1-4
#   v1-1    7/5/2024    Basic structure of program, define functions and main
#   v1-2    7/7/2024    Fill out the functions and debug them
#   v1-3    7/9/2024    Add Dictionaries and datetime object
#   v1-4    7/11/2024   Add the argv parsing and debug write statements
#   v1-5    7/14/2024   Add Dictionary of Dictionaries for Iteration (rows)
#  Comments:
#    Read the input file, line by line, looking for specific patterns in the Convergence Log
#    and create an xlsx file that summarizes each Iteration.  Options "--version" and "--help"
#    are available on the command line.  They are exclusive options (if typed, they print the
#    desired information and exit the program).

# Usage:
#    ReadConvLog.py InputFile [OutputFile] { [--d] | [--d DebugFile] }

# argv[0]:  ReadConvLog.py
# argv[1]:  ConvLogFile.txt is the input file for the v14.1.5 Convergence Log - this is a required argument
# argv[2]:  ConvLogMetrics.xlsx is the output file for each Iteration - this is an optional requirement; if it is
#    ommitted, then "ConvergenceLogMetrics.xlsx" will be the default output excel file
# argv[3]:  -d option tells the program that we want an optional debug file created; if the optional debug file name
#    is missing, then the output will be printed on stdout:
# argv[4]:  Debug file name (optional).  Note that a debug file cannot be given without the -d argument.

# Calls to this program can look like any of the following:
#    ReadConvLog.py PeakWD.log --d
#    ReadConvLog.py PeakWD.log PeakWD_Metrics.xlsx
#    ReadConvLog.py PeakWE.log --d debug.out
#    ReadConvLog.py PeakWE.log PeakWE_Metrics.xlsx --d
#    ReadConvLog.py PeakWD.log PWD_Metrics.xlsx -d debug.out
#    ReadConvLog.py --help
#    ReadConvLog.py --version

# TODO
# - do the datetime arithmatic for Iteration Duration and Running Time; need to read the dictionary
#   values which are datetime objects into datetime variables, do the arithmatic, and then store them
#   in the Duration and Running Time location in the Dictionary
# - see if there is a way to format columns D (Duration) and E (Total Running Time) as time(37:30:55),
#   and column O (Binding Constraint) as Number in the excel dataframe before writing it to a file

#  Function: read_file
#  Purpose:  Read each line in the input file, which is the Convergence Log from Macro 3,
#    corresponding to the v14.1.5 engine.  All of the file reading is done in this function,
#    generally, line by line.  Each line is parsed, looking for a specific string.  If the
#    pattern is found, the logic will save the data in a Dictionary, and then continue to the
#    next line.  In a couple of patterns, the data needed is a couple lines later, so the logic
#    will read the needed lines and extract the data and store it in the Dictionary.


def read_file(inHandle, logDict, summaryDict, DEBUG, debugHandle):
    currIter = 1  # this is the Row Number for the Iteration Dictionaries (each row is a dictionary)
    OPF_SOLUTION_IS_COMPLETED = (
        0  # Need this to print the final duration value for the convergence
    )

    for line in inHandle:
        if parse_ITERATION(
            line, currIter, logDict, DEBUG, debugHandle
        ):  #  Looking for ITERATION, number and timestamp
            continue  #  Go read the next line in the input file

        if parse_SUMMARY(
            line, currIter, summaryDict, DEBUG, debugHandle
        ):  #  Looking for the end of OPF and timestamp
            if DEBUG:
                debugHandle.write(
                    f"OPF SOLUTION IS COMPLETED Value is {OPF_SOLUTION_IS_COMPLETED}"
                )
            if OPF_SOLUTION_IS_COMPLETED:
                logDict[currIter] = {}  #  need one last line in Dictionary
                logDict[currIter]["Iteration"] = "OPF END"
                logDict[currIter]["Date"] = summaryDict[
                    f"ConvergenceSummaryTime {currIter}"
                ]
                logDict[currIter - 1]["Duration"] = (
                    "=C" + str(int(currIter + 1)) + "-C" + str(int(currIter))
                )
                logDict[currIter - 1]["Total Running Time"] = (
                    "=D" + str(int(currIter)) + "+E" + str(int(currIter - 1))
                )
                if DEBUG:
                    debugHandle.write(
                        f'\nIteration Value is { logDict[currIter]["Iteration"] }'
                    )
            continue  #  Go read the next line in the input file

        if parse_OPTIMIZATION(
            line, currIter, summaryDict, DEBUG, debugHandle
        ):  #  Looking for AUC AUX or AUC CCS
            currIter += 1  #  increase Iter count only after Summary or End of OPT
            continue  #  Go read the next line in the input file

        if parse_OPF_START(
            line, DEBUG, debugHandle
        ):  #  Looking for the start of each Iteration's constraints
            # read lines until pattern "Limit Enforcement Summary" pattern is found
            Stopper = 0
            Found = 0
            while not Found:
                newLine = inHandle.readline()
                if "Limit Enforcement Summary" in newLine:
                    Found += 1
                    if DEBUG:
                        debugHandle.write(
                            f"\n{currIter} Found Limit Enforcement Summary - End of ITERATION: { newLine }"
                        )
                    continue
                Stopper += 1
                if (
                    Stopper > 100000
                ):  #  Escape infinite loop just in case this Convergence Log quit early
                    Found = Stopper
                # Future enhancement: count number of FLO, PGG, and BDG and their max values in this Iteration
            continue  #  Go read the next line in the input file

        if parse_VIOLATIONS(
            line, currIter, logDict, DEBUG, debugHandle
        ):  #  Looking for "Incoming Violations" or "No additional violaions"
            continue  #  Go read the next line in the input file

        if parse_BINDING(
            line, currIter, logDict, DEBUG, debugHandle
        ):  #  Looking for "Binding limits" counts"
            continue  #  Go read the next line in the input file

        if parse_OPF_END(
            line, DEBUG, debugHandle
        ):  #  Looking for "OPF - END", then read 3 more lines
            # read 2 lines, print the Objective Function value on the last line
            OPF = inHandle.readline()
            OPF = inHandle.readline()
            tokens = OPF.strip().split()
            if DEBUG:
                debugHandle.write(
                    f"\n{currIter} Objective Function tokens: {tokens[0]}, {tokens[1]}, {tokens[2]}"
                )
            logDict[currIter]["OPF Controls Total"] = int(tokens[0])
            logDict[currIter]["OPF Controls Moved"] = int(tokens[1])
            logDict[currIter]["OPF Objective Function"] = float(tokens[2])
            currIter += 1  #  increase Iter count only after Summary or End of OPT
            continue  #  Go read the next line in the input file

        if parse_COMPLETED(
            line, DEBUG, debugHandle
        ):  #  Looking for "OPF SOLUTION IS COMPLETED"
            OPF_SOLUTION_IS_COMPLETED = 1
            if DEBUG:
                debugHandle.write(
                    f" OPF_SOLUTION_IS_COMPLETED value is {OPF_SOLUTION_IS_COMPLETED}"
                )
            continue  #  Go read the next line in the input file


def parse_string(line):
    parsed_value = line.strip().split()[0]
    return parsed_value


#  Function: parse_ITERATION
#  Purpose:  Find Pattern "ITERATION" and store the iteration number and the timestamp.  The timestamp
#    will be converted to a datetime object and stored in the Dictionary along with the Iteration Number.
#    Note that the Iteration Count (currIter) is not the same as the Iteration Number found in the input
#    file.  Since we do two optimizations for Monthly auctions, we have duplicate Iteration Numbers.
#    Hence, we differentiate the times we see the word "ITERATION" from the pattern in the text line itself.
#  NOTE:  The current Convergence Log does NOT give the year, so it is being forced in this function (2024)
#    until the defect is fixed in the application when creating the Convergence Log file.


def parse_ITERATION(
    line, currIter, logDict, DEBUG, debugHandle
):  #  Looking for ITERATION, number and timestamp
    Found = 0
    if "REPORT: ITERATION" in line:
        Found = 1
        logDict[currIter] = (
            {}
        )  #  nested dictionary - one line of items per row for each iteration
        if DEBUG:
            debugHandle.write(f"\n\n***** {currIter} ***** Found ITERATION:\n{ line }")
        tokens = ""  #  clear buffer
        tokens = (
            line.strip().split()
        )  # Iteration in token[5], month=token[6], day=token[7], time=token[8]
        if DEBUG:
            debugHandle.write(
                f"{currIter} Tokens: {tokens[0]}, {tokens[1]}, {tokens[2]}, {tokens[3]}, {tokens[4]}, {tokens[5]}, {tokens[6]}, {tokens[7]}, {tokens[8]}"
            )

        if len(tokens[5]) < 3:
            logDict[currIter]["Iteration"] = int(tokens[5])
            timestamp = f"{tokens[6]}:{tokens[7]}:2024 {tokens[8]}"
            iterDate = datetime.strptime(timestamp, "%b:%d:%Y %H:%M:%S")
        else:
            logDict[currIter]["Iteration"] = int(tokens[8])
            timestamp = f"{tokens[0]} {tokens[1]}"
            iterDate = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")

        logDict[currIter]["Date"] = iterDate
        if currIter == 1:
            logDict[currIter]["Duration"] = ""
            logDict[currIter]["Total Running Time"] = ""
        else:
            logDict[currIter - 1]["Duration"] = (
                "=C" + str(int(currIter + 1)) + "-C" + str(int(currIter))
            )  # sleezy!!!
            if currIter == 2:
                logDict[currIter - 1]["Total Running Time"] = "=D" + str(int(currIter))
            else:
                logDict[currIter - 1]["Total Running Time"] = (
                    "=D" + str(int(currIter)) + "+E" + str(int(currIter - 1))
                )
    return Found


#  Function: parse_SUMMARY
#  Purpose:  Find Pattern "CONVERGENCE SUMMARY" and its associated timestamp.  When found, the timestamp
#    will be converted to a datetime object so that Excel can read it as a date.  The date object will be
#    stored in the Dictionary here.
#  NOTE:  The current Convergence Log does NOT give the year, so it is being forced in this function (2024)
#    until the defect is fixed in the application when creating the Convergence Log file.
#
def parse_SUMMARY(
    line, currIter, summaryDict, DEBUG, debugHandle
):  #  Looking for the end of the Optimization and timestamp
    Found = 0
    if "CONVERGENCE SUMMARY" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(f"\n{currIter} Found SUMMARY:\n{ line }")
        tokens = ""  #  clear buffer
        tokens = line.strip().split()  # month=tokens[4], day=tokens[5], time=tokens[6]
        if DEBUG:
            debugHandle.write(
                f"{currIter} Tokens: {tokens[0]}, {tokens[1]}, {tokens[2]}, {tokens[3]}, {tokens[4]}, {tokens[5]}, {tokens[6]}"
            )
        timestamp = (
            tokens[4] + " " + tokens[5] + " 2024 " + tokens[6]
        )  #  remove the '2024' when the date bug is fixed
        summaryDate = datetime.strptime(timestamp, "%b %d %Y %H:%M:%S")
        summaryDict[f"ConvergenceSummaryTime {currIter}"] = summaryDate
    return Found


#  Function: parse_OPTIMIZATION
#  Purpose:  Find Pattern "OPTIMIZATION" - this pattern signals that the AUC command has completed, and
#    will save the Optimization options in the Dictionary.
#
def parse_OPTIMIZATION(
    line, currIter, summaryDict, DEBUG, debugHandle
):  #  Looking for AUC AUX or AUC CCS
    Found = 0
    if "OPTIMIZATION : CCS" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(
                f"\n\n ***** {currIter} Found OPTIMIZATION: *****\n{ line }"
            )
        summaryDict[f"ConvergenceSummaryOptions {currIter}"] = line
    return Found


#  Function: parse_OPF_START
#  Purpose:  Find Pattern " OPF - START  " - once this is found, this will trigger the
#    calling function to loop through the file until it finds "OPF END"


def parse_OPF_START(line, DEBUG, debugHandle):
    Found = 0
    if "OPF - START" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(f"\nFound OPF - START\n{ line }")
    return Found


#  Function: parse_OPF_END
#  Purpose:  Find Pattern " OPF - END ", and when this pattern is found, the calling function will
#    then read in a couple more lines to get the Objective Function value and store it in the Dictionary.


def parse_OPF_END(line, DEBUG, debugHandle):
    Found = 0
    if "OPF - END" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(f"\nFound OPF - END\n{ line }")
    return Found


#  Function: parse_VIOLATIONS
#  Purpose:  Find Pattern "Incoming violations" and then get the tokens on the line for the incoming violations.
#    The number of violations for Base Case and Contingency Case are stored in the Dictionary here.
#
def parse_VIOLATIONS(line, currIter, logDict, DEBUG, debugHandle):
    Found = 0
    if "Incoming violations" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(f"\n{currIter} Found VIOLATIONS:\n{ line }")
        tokens = ""  #  clear buffer
        tokens = (
            line.strip().split()
        )  # Total=token[2], BaseCase=token[3], Contingency=token[4]
        if DEBUG:
            debugHandle.write(
                f"{currIter} Tokens: {tokens[0]}, {tokens[1]}, {tokens[2]}, {tokens[3]}, {tokens[4]}"
            )
        logDict[currIter]["Incoming Violations Total"] = int(tokens[2])
        logDict[currIter]["Incoming Violations Base Case"] = int(tokens[3])
        logDict[currIter]["Incoming Violations Contingency"] = int(tokens[4])
    return Found


#  Function: parse_BINDING
#  Purpose:  Find Pattern "Binding limits", and then get the tokens on the line for the binding limits.  The
#    number of violations for the Base Case and Contingency Case are stored in the Dictionary here, as well
#    as the total number of cases analyzed.  Toward the end of the optimization, the total number of cases
#    will stabilize.
#
def parse_BINDING(line, currIter, logDict, DEBUG, debugHandle):
    Found = 0
    if "Binding limits" in line:
        Found = 1
        if DEBUG:
            debugHandle.write(f"\n{currIter} Found BINDING:\n{ line }")
        tokens = ""  #  clear buffer
        tokens = (
            line.strip().split()
        )  # Total=token[2], BaseCase=token[3], Contingency=token[4]
        if DEBUG:
            debugHandle.write(
                f"\n{currIter} Tokens: {tokens[0]}, {tokens[1]}, {tokens[2]}, {tokens[3]}, {tokens[4]}"
            )
        logDict[currIter]["Binding Total"] = int(tokens[2])
        logDict[currIter]["Binding Base Case"] = int(tokens[3])
        logDict[currIter]["Binding Contingency"] = int(tokens[4])
        #  Now the tricky part - want the total number of cases, but sometimes it is not delineated by a space between tokens.
        #  Specifically, tokens[5] can look like "in xxx cases" or "inxxxx cases" depending on the number in xxxx, so we have
        #  to split on "in".  However, the word "in" is found in two places on this line "bINding" and "in".
        Cases = line.split(
            "in"
        )  #  number of cases will be in Cases[3], and it will be the first xxx or xxxx token
        if DEBUG:
            debugHandle.write(f"\n{currIter} Cases = { Cases }")
        if len(Cases) > 3:
            numCases = Cases[3].split()
            if DEBUG:
                debugHandle.write(f"\n{currIter} Number of cases found: { numCases[0]}")
            logDict[currIter]["Total Cases"] = int(numCases[0])
    return Found


#  Function: parse_COMPLETED
#  Purpose:  Find Pattern "  OPF SOLUTION IS COMPLETED    "
#
def parse_COMPLETED(line, DEBUG, debugHandle):
    Found = 0
    if "OPF SOLUTION IS COMPLETED" in line:
        if DEBUG:
            debugHandle.write(f"\n{ line.strip() }")
        Found = 1
    return Found


#  Function: Main
#  Purpose:  Process the arguments on the command line, call function to read the
#    input file, and then print the results in an output file.  The results are
#    stored in the Dictionary called "logDict", which is declared in the Main
#    function and passed as an argument to the read_file function.  The Dictionary
#    is then output in a format that can be opened with excel, although the output
#    file itself is a text file.

if __name__ == "__main__":

    logDict = (
        {}
    )  # dictionary for summarizing each Iteration's metrics; this is a dictionary of dictionaries
    summaryDict = {}  # dictionary for containing the optimization summary timestamp

    # process argv array - there can be up to 4 arguments on the input line, and they are input "in order"
    # argv = PythonScript.pl ConvLogFile.txt ConvLogMetrics.xlsx -d DebugFile.txt

    # Usage:
    #    ReadConvLog.py InputFile [OutputFile] { [--d] | [--d DebugFile] }

    if len(sys.argv) < 2:
        print(
            "Usage: ReadConvLog.py InputFile [OutputFile] { [--d] | [--d DebugFile] }"
        )
        exit()
    else:
        for i in range(len(sys.argv)):
            if "--help" in sys.argv[i]:
                print(
                    "Usage: ReadConvLog.py InputFile [OutputFile] { [--d] | [--d DebugFile] }"
                )
                exit()
            if "--version" in sys.argv[i]:
                print(f"Version: ReadConvLog.py {version}")
                exit()
        for i in range(len(sys.argv)):
            print(f"argv[{ i }] = {sys.argv[i]}")
        inFileName = sys.argv[1]
        baseName = inFileName.rsplit(".", 1)[0]
        outFileName = baseName + "_Metrics.xlsx"
        debugFileName = baseName + "_Debug.out"
        summaryFileName = baseName + "_Summary.xlsx"
        DEBUG = 0

        if len(sys.argv) == 3:  #  py inFile outFile, py inFile --d
            if "--d" in sys.argv[2]:
                DEBUG = 1
            else:
                outFileName = sys.argv[2]
        if len(sys.argv) == 4:  #  py inFile outFile --d, py inFile --d debugFile
            if "--d" in sys.argv[3]:
                DEBUG = 1
                outFileName = sys.argv[2]
            if "--d" in sys.argv[2]:
                DEBUG = 1
                debugFileName = sys.argv[3]
        if len(sys.argv) == 5:  # py inFile outFile --d debugFile
            DEBUG = 1
            debugFileName = sys.argv[4]
            outFileName = sys.argv[2]

    print(f"input file name is { inFileName }")
    if DEBUG:
        print(f"debug file is { debugFileName }")
    print(f"output file name is { outFileName }")
    print(f"summary file name is { summaryFileName }")

    #  Open the files
    try:
        inHandle = open(inFileName, "r")
    except FileNotFoundError:
        print(f"Error: File '{ inFileName }' not found.")
        exit()
    except Exception as e:
        print(f"An error occurred: { e }")
        exit()

    try:
        outHandle = open(outFileName, "w")
    except FileNotFoundError:
        print(f"Error: File '{ outFileName }' not found.")
        exit()
    except Exception as e:
        print(f"An error occurred: { e }")
        exit()

    try:
        summaryFileHandle = open(summaryFileName, "w")
    except FileNotFoundError:
        print(f"Error: File '{ summaryFileName }' not found.")
        exit()
    except Exception as e:
        print(f"An error occurred: { e }")
        exit()

    if DEBUG:
        try:
            debugHandle = open(debugFileName, "w")
        except FileNotFoundError:
            print(f"Error: File '{ debugFileName }' not found.")
            exit()
        except Exception as e:
            print(f"An error occurred trying to open: { e }")
            exit()
    else:
        print(f"WARNING: Debug file not requested.\n")
        debugHandle = 0

    #  Read the input file and create the two dictionaries, one for all of the tokens needed for each ITERATION
    #  and one needed for the timestamp for the End of the Optimization.  Currently (2024), there are two AUC
    #  commands - one for the AUC CCS AUX auxiliary optimization, and one for the AUC CCS optimization.

    read_file(inHandle, logDict, summaryDict, DEBUG, debugHandle)

    #  Print the output files as lists in the debug file
    if DEBUG:
        for key, value in logDict.items():
            debugHandle.write(f"\nKey: { key } | Value: { value }")
        for key, value in summaryDict.items():
            debugHandle.write(f"\nKey: { key } | Value: { value }")

    #  NOTE:  If the excel file is currently open, you will get a "Permission Denied" Error!!!

    #  The order of the Excel header is as follows.  Please note that some of the values in the DataFrame object
    #  are actual computations meant for Excel calculations - so if any of the columns get moved below, you will
    #  need to adjust the arithmetic for the "Duration" and "Total Running Time" cell values in the above code.
    columns = ("Iteration", "Date", "Duration", "Total Running Time")
    columns += (
        "Incoming Violations Total",
        "Incoming Violations Base Case",
        "Incoming Violations Contingency",
    )
    columns += ("Binding Total", "Binding Base Case", "Binding Contingency")
    columns += (
        "Total Cases",
        "OPF Controls Total",
        "OPF Controls Moved",
        "OPF Objective Function",
    )
    df = pd.DataFrame(data=logDict).T
    df.to_excel(outFileName, columns=columns)

    #  Write the summary file - this contains only the start time of the first Iteration 1 and the final END OPF time
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in summaryDict.items()]))
    df.to_excel(summaryFileName, index=False)

    # Close the files and exit the program
    inHandle.close()
    outHandle.close()
    summaryFileHandle.close()
    if DEBUG:
        debugHandle.close()
    exit()
