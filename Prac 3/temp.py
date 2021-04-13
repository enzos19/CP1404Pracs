"""
CP1404 - Practical 2
"""

def main():
    menu  = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input("====").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = convert_celsius()
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
        print(menu)
        choice = input("=== ").upper()
    print("Thank you.")

def convert_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def convert_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

if __name__ == '__main__':
    main()
#