import sys
sys.setrecursionlimit(1500)

def rev(s):
    if len(s) == 1:
        return s
    rv = rev(s[1:])
    return rv + s[0]


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s = str(input())
    print(rev(s))
    return

if __name__ == '__main__':
    main()