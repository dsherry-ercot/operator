monthly_credit_success = 0
monthly_credit_skip = 0
annual_credit_success = 0
annual_credit_skip = 0
monthly_results_success = 0
monthly_results_skip = 0
annual_results_success = 0
annual_results_skip = 0


def monthly_credit_results(monthly_credit_success, monthly_credit_skip):
    print(
        f"{monthly_credit_success} files added to Monthly Credit folder. {monthly_credit_skip} skipped because they already exist"
    )


def annual_credit_results(annual_credit_success, annual_credit_skip):
    print(
        f"{annual_credit_success} files added to Annual Credit folder. {annual_credit_skip} skipped because they already exist"
    )


def monthly_results_results(monthly_results_success, monthly_results_skip):
    print(
        f"{monthly_results_success} files added to Monthly Results folder. {monthly_results_skip} skipped because they already exist"
    )


def annual_results_results(annual_results_success, annual_results_skip):
    print(
        f"{annual_results_success} files added to Annual Results folder. {annual_results_skip} skipped because they already exist"
    )
