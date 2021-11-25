def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(1, n+1):
        s = 0
        n = i
        while n > 0:
            r = n%10
            n = n//10
            s += r*r*r
        if s == i:
            print(i)
    return 0

if __name__ == '__main__':
    main()