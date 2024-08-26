#Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Testing the function

celsius_value = 25
fahrenheit_value = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C is equal to {fahrenheit_value}°F")



