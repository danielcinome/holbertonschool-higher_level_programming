#!/usr/bin/python3
import sys
ran = len(sys.argv)
if ran == 1:
    print('{:d} arguments.'.format(ran - 1))
else:
    print('{} arguments:'.format(ran - 1))
    for i in range(1, ran):
        print('{}: {}'.format(i, sys.argv[i]))
