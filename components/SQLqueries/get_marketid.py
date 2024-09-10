from ercotdb import Database

prod = Database(dbname="PR07CRR")


def get_market_id(name: str) -> int:

    df = prod.query(
        f"""
    select ID
    from HEDGEUSER.FTR_MARKET t
    where name = '{name}'
    """
    )

    return df.loc[0]["id"]


if __name__ == "__main__":
    get_market_id("2024.AUG.Monthly.Auction")
