def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    while (T > 0):
        T -= 1
        A = list(map(int, input().split()[1:]))
        B = int(input())
        if B in A:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()