#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    ran = len(sys.argv)
    a, b = 0, 0
    if ran < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == '+':
                print('{} + {} = {}'.format(a, b, cal.add(a, b)))
            elif sys.argv[2] == '-':
                print('{} - {} = {}'.format(a, b, cal.sub(a, b)))
            elif sys.argv[2] == '*':
                print('{} * {} = {}'.format(a, b, cal.mul(a, b)))
            elif sys.argv[2] == '/':
                print('{} / {} = {}'.format(a, b, cal.div(a, b)))
            else:
                print('Unknown operator. Available operators: +, -, * and /')
                sys.exit(1)
        except ValueError:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
            sys.exit(1)
