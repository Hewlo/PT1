from References.C1L1.L1_1 import redirection
import sys

if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = redirection(in_obj=sys.stdin, out_obj=sys.stdout)

    a = input('Enter a string: ')
    b = input('Enter another string: ')
    print('Entered strings are:', repr(a), 'and', repr(b))