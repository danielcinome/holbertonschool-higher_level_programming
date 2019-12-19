#!/urs/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary.items())
    for i in enumerate(a_dictionary):
        print(i[1][0], ':', i[1][1])
