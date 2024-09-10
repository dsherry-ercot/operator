import smtplib
from email.message import EmailMessage
import datetime
import time
from email.mime.text import MIMEText


def send_email(auction_name, results_folder, convergence_status, iterations, table):

    # craft email
    msg = EmailMessage()
    msg["subject"] = f"{auction_name} Results Ready for Validation"
    msg["From"] = "daniel.sherry@ercot.com"
    msg["To"] = "daniel.sherry@ercot.com"

    content = f"""
Hey esteemed colleague,

Please validate the {auction_name} results. The files are located at {results_folder}. I have already completed the basic validation items below, but we need another operator to validate the results. 

There were two binding constraints with a shadow price exceeding $100k. 

Insert Table

Based on the “Validate CRR Auction Results” procedure, the {auction_name} results look good.

Per CRR Business Process: 
1. Convergence log check --> {convergence_status}
“OPF solution is completed” appears - OPF solution completed in {iterations} iterations

2. Binding constraints check: ensure that the Violation column is “0” for all binding constraints – binding status 

3. PTP Bids and CRRs check: verify that the Awarded MW column is equal to or less than the Bid MW column for each row – Pass
4. Account Holder creditworthiness flag check: ensure that no account holder whose creditworthiness flag was set to “No” received any bids in the auction – Pass
5. Clearing price validation check: ensure that buy bids’ clearing prices are </= bid price, ensure that sell bids’ clearing prices are >/= bid price – Pass 



Daniel Sherry
    """

    msg.set_content(content)

    with smtplib.SMTP("mail.ercot.com") as smtp:
        smtp.ehlo()

        smtp.send_message(msg)


if __name__ == "__main__":
    send_email()
