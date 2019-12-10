#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    l_num = number % 10
    l_num = l_num * -1
    number = number * -1
else:
    l_num = number % 10
if l_num > 5:
    print('Last digit of', number, 'is', l_num, 'and is greater than 5')
elif l_num == 0:
    print('Last digit of', number, 'is', l_num, 'and is 0')
else:
    print('Last digit of', number, 'is', l_num, 'and is less than 6 and not 0')
