import smtplib
import datetime as dt
import random


def send_email(quote):
    my_email = "testemail.ksg.data@gmail.com"
    app_password = "tjfe xxdk yojh xpuc"

    # recipient test email
    to_email = "testemailksg.data@yahoo.com"

    # create SMTP object, takes smtp server as input
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # call tls - transport layer security - encrypts connection
        connection.starttls()
        # then login with credentials
        connection.login(user=my_email, password=app_password)
        # now send email - to, from, msg all required
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Happy Monday!\n\nHere's your quote for the week:\n{quote}"

        )


def main():
    now = dt.datetime.now()

    if now.weekday() == 3:
        with open("quotes.txt", "r") as file:
            quote = file.readlines()
            pick = random.choice(quote)
            send_email(pick)


main()



