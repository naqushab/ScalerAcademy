def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(2*n):
        if i < n:
            st = n - i
            for s in range(st):
                print('*', end='')
            for b in range(2*i):
                print(' ', end='')
            for s in range(st):
                print('*', end='')
        elif i >= n:
            st = i - n + 1
            for s in range(st):
                print('*', end='')
            for b in range(2*n-2*st):
                print(' ', end='')
            for s in range(st):
                print('*', end='')
        print() 
    return 0

if __name__ == '__main__':
    main()