import smtplib

def email_setup():
    with open('email.txt', 'r') as email:
        var = email.readlines()

    my_email = list()
    for line in var:
        line = line.replace("\n", "")
        my_email.append(line)
        
    return my_email

def email_sending(my_email, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email[0], password=my_email[1])
        connection.sendmail(from_addr=my_email,
                            to_addrs="jagaw31633@godsigma.com",
                            msg=f"Subject:ISSOverhead\n\n{msg}")
    print("email sent")