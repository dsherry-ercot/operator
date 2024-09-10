import time, functions
from pathlib import Path
import logging

log_format = "%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename="MWHs\MWHs.log",
    format=log_format,
    level=logging.INFO,
    datefmt=date_format,
    filemode="w",
)


def run_monthly():
    logging.info("Starting Monthly MWHs pull")
    start_time = time.time()

    directory = Path(str("Q:\CRR GoLive\Auction_Files\Monthly_Auctions"))
    for year_folder in directory.iterdir():
        if "202" in str(year_folder):
            for month_folder in Path(directory, year_folder).iterdir():
                # if "JUL" in str(month_folder):
                try:
                    results_folder = Path(
                        directory, year_folder, month_folder, "Results"
                    )
                    logging.info(f"Grabbing data from: {month_folder}")
                    functions.build_df_month(str(results_folder), month_folder)
                except Exception as e:
                    print(f"{month_folder} threw an exception")
                    print(e)
                    logging.error("Could not open and read file specified")
                    continue

    function_time = time.time() - start_time
    print(f"This took {function_time} seconds")


def run_ltas():
    logging.info("Starting LTAS MWHs pull")
    start_time = time.time()

    directory = Path(str("Q:\CRR GoLive\Auction_Files\LTAS_Auctions"))
    for year_folder in directory.iterdir():
        # if "LTAS23" in str(year_folder):
        for ltas_auction in Path(directory, year_folder).iterdir():
            # if "Seq6" in str(ltas_auction):
            try:
                results_folder = Path(directory, year_folder, ltas_auction, "Results")
                print(f"Grabbing data from: {ltas_auction}")
                logging.info(f"Grabbing data from: {ltas_auction}")
                functions.build_df_ltas(str(results_folder), ltas_auction)
            except Exception as e:
                print(f"{ltas_auction} threw an exception")
                print(e)
                logging.error("Could not open and read file specified")
                continue

    function_time = time.time() - start_time
    print(f"This took {function_time} seconds")
    logging.info(f"This took {function_time} seconds")


if __name__ == "__main__":
    run_ltas()
    run_monthly()
