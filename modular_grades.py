# Alexander J. Jackson 
# modular_grades.py

# returns grade
def get_grade():
    grade = int(input("Enter a grade between 0 and 100: "))
    return grade

# prints letter grade
def letter_grade(p):
    if p >= 90:
        result = "A"
        print(f"You passed with a Grade {result}")
    elif p > 80 and p < 90:
        result = "B"
        print(f"You passed with a Grade {result}")
    elif p > 70 and p < 80:
        result = "C"
        print(f"You passed with a Grade {result}")
    elif p > 60 and p < 70:
        result = "D"
        print(f"You passed with a Grade {result}")
    else:
        print("You Failed")
    
def main():
    
    # input section for get_grade()
    grade1 = get_grade()
    grade2 = get_grade()
    grade3 = get_grade()

    # declaration of total & percentage
    total = grade1 + grade2 + grade3
    percentage = total / 3
    print(f"Your final grade percentage is {percentage}")

    # calling letter_grade()
    letter_grade(percentage)




main()



