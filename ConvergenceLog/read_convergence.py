import pandas as pd
from datetime import datetime
import logging

log_format = "%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename=r"ConvergenceLog\app.log",
    format=log_format,
    level=logging.INFO,
    datefmt=date_format,
    filemode="w",
)


def parse_convergence_log(file_path):
    logging.info(f"File path specified: {file_path}")
    final_result = []
    year = get_year(file_path)
    try:
        with open(file_path, "r") as doc:
            content_as_lst = doc.readlines()  # read all lines, put in a big list
            iter_lst = iter(  # make list iterable so we can view line by line
                content_as_lst
            )
    except:
        logging.error("Could not open and read file specified")
        exit()
    logging.info("File opened successfully")
    for line in iter_lst:
        if "REPORT: ITERATION" in line:
            result = []
            parse_iteration(line, year, result)
        if "Incoming violations" in line:
            parse_violations(line, result)
        if "Binding limits" in line:
            parse_binding(line, result)
        if "OPF - END" in line:
            # get two lines after 'OPF - END' line
            line = next(iter_lst)
            line = next(iter_lst)
            parse_OPF_end(line, result)
            logging.info(result)
            final_result.append(result)
        # if "CONVERGENCE SUMMARY" in line:
        #     parse_summary(line, year, result)
        # if "Incoming violations" in line:
        #     parse_optimization(line, result)
    # print(final_result)
    df = convert_to_df(
        final_result
    )  # turn lists into DataFrame (which is just a table)

    try:
        output_to_excel(df, file_path)  # output table to Excel file
    except:
        logging.error(
            f"Error occured. Ensure file is not open so Python can use it.",
            exc_info=True,
        )
    else:
        logging.info("Excel file generated successfully")


def get_year(file_path):
    year = file_path.split("\\")[-1][:4]
    return year


def parse_summary(line, year, result):
    tokens = line.strip().split()
    summaryDate = parse_date(tokens[4], tokens[5], year, tokens[6])

    # print(summaryDate)


def parse_optimization(line, result):
    if "OPTIMIZATION : CCS" in line:
        pass


def parse_violations(line, result):
    tokens = line.strip().split()
    result.append(int(tokens[2]))  # Incoming Violations Total
    result.append(int(tokens[3]))  # Incoming Violations Base Case
    result.append(int(tokens[4]))  # Incoming Violations Contingency

    # print(result)
    return result


def parse_binding(line, result):
    tokens = line.strip().split()
    result.append(int(tokens[2]))  # Binding Total
    result.append(int(tokens[3]))  # Binding Base Case
    result.append(int(tokens[4]))  # Binding Contingency
    result.append(int(tokens[6]) if len(tokens) > 5 else None)  # Total Cases
    return result


def parse_OPF_end(line, result):
    tokens = line.strip().split()
    result.append(int(tokens[0]))  # OPF Controls Total
    result.append(int(tokens[1]))  # OPF Controls Moved
    result.append(float(tokens[2]))  # OPF Objective Function
    return result


def parse_iteration(line, year, result):
    tokens = line.strip().split()
    if len(tokens[5]) < 3:
        result.append(int(tokens[5]))  # save iteration number
        result.append(  # save datetimestamp
            parse_date(tokens[6], tokens[7], year, tokens[8])
        )
    else:
        result.append(int(tokens[8]))
        timestamp = f"{tokens[0]} {tokens[1]}"
        result.append(datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S"))

    return result


def parse_date(month, day, year, time):
    datetimestamp = f"{month}-{day}-{year} {time}"
    date = datetime.strptime(datetimestamp, "%b-%d-%Y %H:%M:%S")
    return date


def convert_to_df(final_result):
    df = pd.DataFrame(
        final_result,
        columns=[
            "Iteration",
            "Date",
            "Incoming Violations Total",
            "Incoming Violations Base Case",
            "Incoming Violations Contingency",
            "Binding Total",
            "Binding Base Case",
            "Binding Contingency",
            "Total Cases",
            "OPF Controls Total",
            "OPF Controls Moved",
            "OPF Objective Function",
        ],
    )

    return df


def output_to_excel(df, file_path):
    workbook_title = file_path.split("\\")[-1][:-4]

    with pd.ExcelWriter(
        f"{workbook_title}_Metrics.xlsx",
        engine="xlsxwriter",
        datetime_format="YYYY-MM-DD HH:MM",
    ) as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Metrics",
        )
        worksheet = writer.sheets["Metrics"]
        workbook = writer.book

        format = workbook.add_format(
            {"align": "center", "border": 1, "text_wrap": True}
        )
        worksheet.set_column("A:N", None, format)

        worksheet.autofit()


if __name__ == "__main__":
    parse_convergence_log(
        r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results\2024.AUG.Monthly.Auction_PeakWD.log"
    )
