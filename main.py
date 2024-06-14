##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

PLACEHOLDER = "[NAME]"


def write_email(person_name, email_add):
    name = person_name
    email = email_add
    pick = random.randint(1,3)
    template = f"letter_templates/letter_{pick}.txt"
    with open(template) as file:
        content = file.read()

        new_email = content.replace(PLACEHOLDER, name)
        send_email(email, new_email)


def send_email(email_add, e_content):
    my_email = "testemail.ksg.data@gmail.com"
    app_password = "tjfe xxdk yojh xpuc"
    to_email = email_add
    body = e_content

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: HAPPY BIRTHDAY\n\n{body}"
        )


def main():
    now = dt.datetime.now()
    # print(now.month, now.day)
    bday = pd.read_csv("birthdays.csv", index_col=False)

    for (index, row) in bday.iterrows():
        if row.month == now.month and row.day == now.day:
            name = bday.iloc[row.name]["name"]
            email = bday.iloc[row.name]["email"]

            write_email(name, email)



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


if __name__ == '__main__':
    main()


