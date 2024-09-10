from datetime import datetime

tokens_old = [
    "04/12/2023",
    "11:14:26",
    "CPT",
    "MULTI_PERIOD",
    "AUCTION",
    "CONVERGENCE",
    "REPORT",
    "ITERATION",
    "1",
]
tokens_new = [
    "MULTI-PERIOD",
    "AUCTION",
    "CONVERGENCE",
    "REPORT:",
    "ITERATION",
    "1",
    "JUL",
    "19",
    "11:36:14",
]


def vickitest(tokens):
    if len(tokens[5]) < 3:
        iteration = int(tokens[5])
        timestamp = f"{tokens[6]}:{tokens[7]}:2024 {tokens[8]}"
        iterDate = datetime.strptime(timestamp, "%b:%d:%Y %H:%M:%S")
        print(f"New Format: {iteration=} {timestamp=} {iterDate=}")
    else:
        iteration = int(tokens[8])
        timestamp = f"{tokens[0]} {tokens[1]}"
        iterDate = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        print(f"Old Format: {iteration=} {timestamp=} {iterDate=}")


vickitest(tokens_old)
vickitest(tokens_new)
