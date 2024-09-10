import subprocess

def open_monthly_tc():
    subprocess.Popen(r'explorer  "C:\Users\dsherry\ERCOT\Congestion Analysis and Revenue Rights - Team Library\CRR Auction Task Completion (TC) Logs\Monthly Auctions and True-Up Allocations\2024 Auctions and Allocations"')

def open_annual_tc():
    subprocess.Popen(r'explorer "C:\Users\dsherry\ERCOT\Congestion Analysis and Revenue Rights - Team Library\CRR Auction Task Completion (TC) Logs\Long Term Sequence Auctions (Restructured Auctions NPRR463)"')

if __name__ == "__main__":
    open_monthly_tc()