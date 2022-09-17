from datetime import datetime
import smtplib
import pandas
import random

my_email = "adityakumar5443321@gmail.com"
my_pass = "mjjnoutlppzslctx"

today = datetime.now()
today_tuple = (today.month,today.day)
# print(today_tuple)

data = pandas.read_csv("birthdays.csv")
# print(data)
birthday_dic = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dic :
    birthdday_person = birthday_dic[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as msg:
        messege = msg.read()
        messege1 = messege.replace("[NAME]",birthdday_person["name"])
        print(messege1)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,to_addrs=birthdday_person["email"],msg=f"Subject:Happpy Birthday!\n\n{messege1}")