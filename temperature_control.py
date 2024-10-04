
# Alexander J. Jackson
# temperature_control.py

def celsius_to_fahrenheit(celsius):
    step_1 = 9 / 5
    step_2 = celsius * step_1
    step_3 = step_2 + 32
    return step_3

def fahrenheit_to_celsius(fahrenheit):
    step_1 = 5 / 9
    step_2 = fahrenheit - 32
    step_3 = step_2 * step_1
    return step_3

def main():
    request = int(input("'1' to convert Celsius to Fahrenheit or '2' to convert Fahrenheit to Celsius: "))

    if request == 1:
        temperature = int(input("Enter temperatur in Celsius: "))
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature: .2f}C is equal to {result: .2f}F")

    elif request == 2:
        temperature = int(input("Enter temperatur in Fahrenheit: "))
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature: .2f}F is equal to {result: .2f}C")
main()
