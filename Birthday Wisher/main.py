import smtplib, random, pandas
from datetime import datetime

MY_EMAIL = ""
PASSWORD = ""

# Create a TUPLE representing current month and current day of month
TODAY_TUPLE = (datetime.now().month, datetime.now().day)

# Read the birthday.csv ---- name,email,year,month,day
data = pandas.read_csv("birthdays.csv")

# Using dictionary comprehension to create a dictionary in certain order (birthday_month,birthday_day):row
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# Check if today_tuple matches in new_dict
if TODAY_TUPLE in birthday_dict:
    # Provide a path from random letter template
    letter_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        letter_contents = letter_file.read()
        # Replace the placeholder [NAME] in the template with the corresponding name from the birthday_dict
        new_letter = letter_contents.replace("[NAME]", birthday_dict[TODAY_TUPLE]["name"])
    # Open a connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure the connection
        connection.starttls()
        # Login using the declared global constants
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            # Corresponding email address from the birthday_dict
                            to_addrs=birthday_dict[TODAY_TUPLE]["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")