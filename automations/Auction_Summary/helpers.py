import glob
from pathlib import Path


def get_file_path(auction_name):
    results_path = get_results_path(auction_name)
    return list(Path.glob(results_path, "*BidsOffersAndCRR*fter*csv"))[0]


def get_results_path(auction_name: str) -> str:
    if "annual" in auction_name.lower():
        directory = Path(str("Q:\CRR GoLive\Auction_Files\LTAS_Auctions"))
        parent_folder = list(Path.glob(
            directory, rf"*\*{auction_name.replace('.', '_').replace('Auction', '')}*"))[0]
        results_folder = Path(parent_folder, "Results")
    elif "month" in auction_name.lower():
        month_folder = get_month_folder_name(auction_name)
        directory = Path(str("Q:\CRR GoLive\Auction_Files\Monthly_Auctions"))

        year_folder = auction_name[:4]
        results_folder = Path(
            directory, year_folder, month_folder, "Results"
        )
    return results_folder


def get_month_folder_name(auction: str = "2024.AUG.Monthly.Auction") -> str:
    """
    Turns "2024.AUG.Monthly.Auction" into "2024_08_AUG"
    """
    year = auction[:4]
    month = auction[5:8]
    month_number = month_dict[month]
    return f"{year}_{month_number}_{month}"


def get_ltas_folder_name(auction: str) -> str:
    """ 
    Turns "2026.1st6.AnnualAuction.Seq4" into "LTAS23 (2024.2nd6 - 2027.1st6)"
    """
    pass


month_dict = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
}

if __name__ == "__main__":
    get_file_path("2024.AUG.Monthly.Auction")
