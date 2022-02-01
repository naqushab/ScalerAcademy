def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    arr = input()
    l = list(map(int, arr.split(' ')))
    print(max(l) + " " + min(l))
    return 0

if __name__ == '__main__':
    main()