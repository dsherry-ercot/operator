import pandas as pd

df = pd.read_excel('data/Activity_Calendar.xlsx')

def get_capacity(new_auction_name):
    capacity = df.loc[df["Auction Name"] == new_auction_name, "Auction Capacity %"]
    return capacity.item()

def get_period_name(new_auction_name):
    month = new_auction_name[5:8]
    year = new_auction_name[0:4]
    return month + "_" + year


from datetime import date, timedelta
def get_psadders_day_before(new_auction_name):
    
    day = df.loc[df["Auction Name"] == new_auction_name, "Post Path Specific Adders Report"]
    timestamp = day.item()
    prev_day = timestamp.date() - timedelta(days=1)
    return date.strftime(prev_day, "%m/%d/%Y 12:00 AM")

def get_notice_date(new_auction_name):
    day = df.loc[df["Auction Name"] == new_auction_name, "Post Auction Notice and Credit Window Opens"]
    timestamp = day.item()
    tdate = timestamp.date()
    return date.strftime(tdate, "%m/%d/%Y 12:00 AM")

def get_open_date(new_auction_name):
    day = df.loc[df["Auction Name"] == new_auction_name, "Auction Bid Window Opens 12:01am"]
    timestamp = day.item()
    tdate = timestamp.date()
    return date.strftime(tdate, "%m/%d/%Y 12:01 AM")

def get_close_date(new_auction_name):
    day = df.loc[df["Auction Name"] == new_auction_name, "Credit Lock Date and Auction Bid Window  Closes 5:00pm "]
    timestamp = day.item()
    tdate = timestamp.date()
    return date.strftime(tdate, "%m/%d/%Y 05:00 PM")
    
