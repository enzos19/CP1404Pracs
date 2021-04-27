
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
for key, value in CODE_TO_NAME.items():
    print("{:3} is {}".format(key, value))

state_type = input("Enter short state: ").upper()
while state_type != "":
    if state_type in CODE_TO_NAME:
        print(state_type, "is", CODE_TO_NAME[state_type])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

