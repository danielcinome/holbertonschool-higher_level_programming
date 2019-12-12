#!/usr/bin/python3
import sys
ran = len(sys.argv)
res = 0
if ran == 1:
    print('{:d}'.format(ran - 1))
else:
    for i in range(1, ran):
        res += int(sys.argv[i])
    print('{}'.format(res))
