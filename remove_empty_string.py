
# Alexander J. Jackson
# remove_empty_string.py

list1 = ['', ' a ', 'b', ' ', 'c ']
list2 = ['d', '   ', 'efg', ' ', 'h i']
list3 = ['jk', 'lm', 'b', '     ', 'n o', '     ']

def remove_empty_strings(bloat_list):
    new_list = []
    for x in bloat_list:
        y = x.strip()
        if y == "":
            pass
        else:
            new_list.append(x)
    return new_list

def main():
    new_list1 = remove_empty_strings(list1)
    new_list2 = remove_empty_strings(list2)
    new_list3 = remove_empty_strings(list3)
    print(new_list1)
    print(new_list2)
    print(new_list3)

main()
