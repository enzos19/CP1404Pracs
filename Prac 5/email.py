def obtain_name(email):
    name = email.split("@")[0]
    part = name.split(".")
    name = " ".join(part).title()
    return name

def main():
    email = input("Email: ")
    mail_name = {}
    while email != "":
        name = obtain_name(email)
        username = input("Is your name {}? (Y/n) ".format(name)).upper()
        if username.upper() == "N" or username.upper() != "Y":
            name = input("Enter your name: ")
        email = input("Email: ")
        mail_name[email] = name
    for email, name in mail_name.items():
        print("{} ({})".format(name, email))
main()