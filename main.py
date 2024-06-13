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
        # print(content)
        new_email = content.replace(PLACEHOLDER, name)
        # send_email(new_email)
        print(new_email)

def send_email(email):
    pass


def main():
    now = dt.datetime.now()
    # print(now.month, now.day)
    bday = pd.read_csv("birthdays.csv", index_col=False)
    # print(bday)
    for (index, row) in bday.iterrows():
        if row.month == now.month and row.day == now.day:
            name = bday.iloc[row.name]["name"]
            email = bday.iloc[row.name]["email"]

            write_email(name, email)
            # birthday_info = bday.loc(row.name)
            # print(bday.iloc[row.name])



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


if __name__ == '__main__':
    main()


