import math

FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = int(input("Enter the temperature to convert: "))
type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if (temp != None):
    match type:
        case "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        case "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")