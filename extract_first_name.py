
# Alexander J. Jackson
# extract_first_name.py

def extract_first_name(names):
    split_names = names.split()
    result = split_names[0]
    return result

def main():
    full_name = input("Please enter your full name: ")
    first_name = extract_first_name(full_name)
    print(f"Your first name is: {first_name}")

main()
