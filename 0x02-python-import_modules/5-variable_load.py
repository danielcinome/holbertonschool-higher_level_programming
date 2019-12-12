#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    for i in dir(variable_load_5):
        if i[0] == "a":
            print('{}'.format(variable_load_5.a))
