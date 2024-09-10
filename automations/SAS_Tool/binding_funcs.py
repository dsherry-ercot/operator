import polars as pl
import streamlit as st


def violation(file_path):
    data = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["violation"])
        .sum()
        .collect()
    )
    sum_violation = data["violation"][0]
    status = "PASS" if data["violation"][0] == 0 else "FAIL"

    return (
        st.markdown("**Binding Constraints**"),
        st.markdown(
            f"23. {sum_violation} violations in Binding Constraints file -> {status}"
        ),
    )


def shadow_price(file_path):
    data = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["shadowprice"])
        .filter(pl.col("shadowprice") < 0)
        .count()
        .collect()
    )
    shadow_prices_below_zero = data[0, 0]
    status = "PASS" if shadow_prices_below_zero == 0 else "FAIL"

    return st.markdown(f"24. {shadow_prices_below_zero} Shadow Prices < 0 -> {status}")


def high_shadow_prices(file_path):
    data = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        # .select(["shadowprice"])
        .filter(pl.col("shadowprice") > 100000).collect()
    )

    high_shadow_prices = data.shape[0]

    return (
        st.markdown(
            f"25. {high_shadow_prices} binding constraint with Shadow Price > 100,000"
        ),
        st.dataframe(data, hide_index=True),
    )


if __name__ == "__main__":
    high_shadow_prices(
        r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results\7832_BindingConstraint.csv"
    )
