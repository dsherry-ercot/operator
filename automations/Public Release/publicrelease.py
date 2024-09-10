# This is an attempt at automating Market Operator procedure 5.1.6
import os
import shutil
import time

from funcs import *
from admin import *
from constants import month_directory, ltas_directory
import data
import create_sic_limits
import zipit

start_time = time.time()

# make_folders()


# for folder in os.listdir(month_directory):
#     if "Annual" not in folder:
#         file_suffix = get_file_suffix_monthly(folder)
#         for file in os.listdir(os.path.join(month_directory, folder, "Credit")):
#             if (
#                 "AHCreditExposure_Before" in file
#                 or "CtPartyCreditExposure_Before" in file
#             ):
#                 file_path = os.path.join(month_directory, folder, "Credit", file)
#                 dst = str(os.path.join(credit, monthly, file[:-4] + file_suffix))

#                 if not os.path.exists(dst):
#                     shutil.copy(file_path, dst)
#                     monthly_credit_success += 1
#                 else:
#                     monthly_credit_skip += 1


# for folder in os.listdir(ltas_directory):
#     for subfolder in os.listdir(os.path.join(ltas_directory, folder)):
#         if "2023" in subfolder:
#             for file in os.listdir(
#                 os.path.join(ltas_directory, folder, subfolder, "Credit")
#             ):
#                 file_suffix = get_file_suffix_ltas(subfolder)
#                 print(file_suffix)
#                 print(os.path.join(ltas_directory, folder, subfolder, "Credit"))
#                 if ("AHCreditExposure" in file and "_After" not in file) or (
#                     "CtPartyCreditExposure" in file and "_After" not in file
#                 ):
#                     file_path = os.path.join(
#                         ltas_directory, folder, subfolder, "Credit", file
#                     )
#                     dst = str(os.path.join(credit, ltas, file[:-4] + file_suffix))
#                     print(file_path, dst)
#                     if not os.path.exists(dst):
#                         shutil.copy(file_path, dst)
#                         annual_credit_success += 1
#                     else:
#                         annual_credit_skip += 1


# # Step 5:
# for folder in os.listdir(month_directory):
#     if "Annual" not in folder:
#         file_prefix = get_file_prefix_monthly(folder)
#         for file in os.listdir(os.path.join(month_directory, folder, "Results")):
#             if "osted" in file:
#                 df = data.drop_portfolio_column(
#                     os.path.join(month_directory, folder, "Results", file)
#                 )
#                 dst = str(os.path.join(bidsCRRs, monthly, file_prefix + file[4:]))
#                 if not os.path.exists(dst):
#                     df.write_csv(dst)
#                     monthly_results_success += 1
#                 else:
#                     monthly_results_skip += 1

# for folder in os.listdir(ltas_directory):
#     for subfolder in os.listdir(os.path.join(ltas_directory, folder)):
#         if "2023" in subfolder:
#             for file in os.listdir(
#                 os.path.join(ltas_directory, folder, subfolder, "Results")
#             ):
#                 file_prefix = get_file_prefix_ltas(subfolder)
#                 if "osted" in file:
#                     df = data.drop_portfolio_column(
#                         os.path.join(ltas_directory, folder, subfolder, "Results", file)
#                     )
#                     dst = str(os.path.join(bidsCRRs, ltas, file_prefix + file[4:]))
#                     if not os.path.exists(dst):
#                         df.write_csv(dst)
#                         annual_results_success += 1
#                     else:
#                         annual_results_skip += 1

# monthly_credit_results(monthly_credit_success, monthly_credit_skip)
# annual_credit_results(annual_credit_success, annual_credit_skip)
# monthly_results_results(monthly_results_success, monthly_results_skip)
# annual_results_results(annual_results_success, annual_results_skip)

# data.write_janjun_monthly_BidsCrrs()
# data.write_juldec_monthly_BidsCrrs()
# data.write_seq1_seq2()
# data.write_seq3_seq4()
# data.write_seq5_seq6()
create_sic_limits.write_month()
# create_sic_limits.write_ltas()
# zipit.zip_files()

function_time = time.time() - start_time
print(f"This took {function_time} seconds")

# Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2023\2023_01_JAN\Credit
