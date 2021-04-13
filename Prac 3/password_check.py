"""
CP1404 - Practical 2
"""

def main():
    symbol = "*"
    password = get_password()
    while not isvalid_password(password):
        print("Invalid password!")
        password = get_password()
    print("Your pasword {}-is a valid password ".format(password))

def get_password():
    print("Please enter your password")
    print("Your password must contain:")
    print("\tone or more uppercase characters")
    print("\tone or more lowercase characters")
    print("\tone or more special characters")
    print("\tone or more numbers")
    password = input(":")
    return password

def isvalid_password(password):
    valid_password = False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if len(password) <= 0 :
        return False
    for char in password :
        if char.isdigit():
            count_digit += 1
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if not char.isalnum():
            count_special += 1
        if count_upper >= 1 and count_lower >= 1 and count_digit >= 1 and count_special >= 1:
            valid_password = True
    return valid_password

if __name__ == '__main__':
    main()