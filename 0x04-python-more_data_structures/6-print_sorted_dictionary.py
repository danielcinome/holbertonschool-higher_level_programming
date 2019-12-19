#!/urs/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = list(sorted(a_dictionary.keys()))
    for i in new:
        print("{}: {}".format(new[1], a_dictionary[i]))
