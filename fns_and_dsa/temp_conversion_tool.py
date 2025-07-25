# temp_conversion_tool.py

CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temp_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_input)
    except:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif unit == 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()

