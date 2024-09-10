import smtplib
from email.message import EmailMessage
from ercotdb import Database
import sql_conn
import time
import schedule
from datetime import datetime

prod = Database("PR07CRR")

market_id = 7869
auction = "2026.2nd6.AnnualAuction.Seq5"


def send_email():
    now = datetime.now().strftime('%I:%M%p')
    total_credit_locked, CPs_with_locked_credit = sql_conn.get_cp_results(
        market_id)
    CRRAHs_with_submitted_bids, bid_count = sql_conn.get_CRRAH_results(
        market_id)

    # craft email
    msg = EmailMessage()
    msg["subject"] = f"(automated test) {auction} Status"
    msg["From"] = "daniel.sherry@ercot.com"
    # , james.allen@ercot.com, samantha.findley@ercot.com, vicki.scott@ercot.com
    msg["To"] = "daniel.sherry@ercot.com"

    content = f"""
    As of {now}:    

    {CPs_with_locked_credit} CPs have locked {total_credit_locked.strip()} total credit.
    {CRRAHs_with_submitted_bids} CRRAH's have submitted {bid_count.strip()} total transactions.

    Don't save this for your records. Dan will manually send out this email once numbers are verified.

    Daniel Sherry
    """

    msg.set_content(content)

    with smtplib.SMTP("mail.ercot.com") as smtp:
        smtp.ehlo()
        smtp.send_message(msg)


send_email()

if __name__ == "__main__":
    schedule.every().day.at("08:00").do(send_email)
    schedule.every().day.at("11:00").do(send_email)
    schedule.every().day.at("15:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
