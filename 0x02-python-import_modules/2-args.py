#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ran = len(sys.argv)
    if ran == 1:
        print('{:d} arguments.'.format(ran - 1))
    else:
        print('{:d} arguments:'.format(ran - 1))
        for i in range(1, ran):
            print('{:d}: {:s}'.format(i, sys.argv[i]))
