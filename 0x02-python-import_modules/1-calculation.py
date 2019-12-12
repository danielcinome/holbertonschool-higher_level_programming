#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    import calculator_1 as cal
    print('{} + {} = {}'.format(a, b, cal.add(int(a), int(b))))
    print('{} - {} = {}'.format(a, b, cal.sub(int(a), int(b))))
    print('{} * {} = {}'.format(a, b, cal.mul(int(a), int(b))))
    print('{} / {} = {}'.format(a, b, cal.div(int(a), int(b))))
