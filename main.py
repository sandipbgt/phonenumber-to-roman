#!/usr/bin/python3

import sys
from six import u
import argparse

def print_red(words):
    print(u("\033[31m\033[49m%s\033[0m") % words)

def print_teal(words):
    print(u("\033[36m\033[49m%s\033[0m") % words)

def to_natural(phone):
    p = []
    for digit in phone.split():
        if digit not in ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
            print_red("Invalid phone number")
            sys.exit(1)

        if digit == '0':
            p.append('0')
        elif digit == 'I':
            p.append('1')
        elif digit == 'II':
            p.append('2')
        elif digit == 'III':
            p.append('3')
        elif digit == 'IV':
            p.append('4')
        elif digit == 'V':
            p.append('5')
        elif digit == 'VI':
            p.append('6')
        elif digit == 'VII':
            p.append('7')
        elif digit == 'VIII':
            p.append('8')
        elif digit == 'IX':
            p.append('9')
    return ''.join(p)

def to_roman(phone):
    p = []
    for digit in phone:
        try:
            if int(digit) not in list(range(0,10)):
                print_red("Invalid phone number")
                sys.exit(1)
        except ValueError:
            print_red("Invalid phone number")
            sys.exit(1)

        if digit == '0':
            p.append('0')
        elif digit == '1':
            p.append('I')
        elif digit == '2':
            p.append('II')
        elif digit == '3':
            p.append('III')
        elif digit == '4':
            p.append('IV')
        elif digit == '5':
            p.append('V')
        elif digit == '6':
            p.append('VI')
        elif digit == '7':
            p.append('VII')
        elif digit == '8':
            p.append('VIII')
        elif digit == '9':
            p.append('IX')
    return ' '.join(p)

def main():
    # roman = to_roman('9842397364')
    # natural = to_natural(roman)
    # print(roman)
    # print(natural)

    parser = argparse.ArgumentParser(description="Utility tool to convert phone number to roman and vice versa.")
    parser.add_argument('phone', help='Phone number.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--roman', action='store_true', help='Convert phone number to roman number.')
    group.add_argument('-n', '--natural', action='store_true', help='Convert phone number to natural number.')

    args = parser.parse_args()

    if args.roman:
        print_teal(to_roman(args.phone))
    elif args.natural:
        print_teal(to_natural(args.phone))
    else:
        parser.print_usage()

if __name__ == '__main__':
    main()