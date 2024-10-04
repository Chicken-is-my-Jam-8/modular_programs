
# Alexander J. Jackson
# nested_loop.py

outer_loop = int(input("Enter range of outside loop: "))
inside = 4 #range of inner loop
total = 0 #start
cycles = 0

for i in range(outer_loop):
    print(f"outer loop value: {i + 1}")
    for t in range(inside):
        total += int(input("Enter something: "))
        cycles += 1

print(f"Total cycles: {cycles}")
print(f"Total: {total}")



