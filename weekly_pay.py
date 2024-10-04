
# Alexander J. Jackson
# weekly_pay.py

# Calculates weekly pay input
def get_input():
    wage = int(input("Please enter wage: "))
    hours = int(input("Please enter hours worked: "))
    if hours > 40:
        pay_1 = wage * hours
        pay = pay_1 * 1.1
        return pay
    else:
        pay = wage * hours
        return pay

# Prints weekly pay
def weekly_pay():
    pay = get_input()
    print(f"Weekly pay: $ {pay}")

weekly_pay()
