
# Alexander J. Jackson
# letter_grade.py

def main():

	total_grade = 0
	for x in range(3):
		total_grade += get_grade()
	grade_average = total_grade / 3

	letter_grade(grade_average)

def get_grade():
	percentage = int(input("Enter a grade between 0 and 100: "))
	return percentage

def letter_grade(percentage_grade):
	print(f"Your final grade percentat is {percentage_grade}")
	if percentage_grade == 75.0:
		print("You passed with a Grade C")

main()
