import smtplib
my_email = "email_addrs"
my_pass = "Password_input"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="anotherEmailAddrs", msg="hello")
