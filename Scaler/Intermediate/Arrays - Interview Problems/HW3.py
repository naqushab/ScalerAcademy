def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    s, e = 0, n-1
    for i in range(n):
        if i == 0 or i == n-1:
            for _ in range(s, e+1):
                print('*', end='')
            e -= 1
        else:
            for c in range(s, e+1):
                if c == s or c == e:
                    print('*', end='')
                else:
                    print(' ', end='')
            e -= 1
        print()
    return 0

if __name__ == '__main__':
    main()