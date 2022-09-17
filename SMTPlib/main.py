import smtplib
my_email = "adityakumar5443321@gmail.com"
my_pass = "mjjnoutlppzslctx"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="aaditya1392@gmail.com", msg="hello")
