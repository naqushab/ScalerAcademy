import math

def is_perfect(n):
    s = 0
    for i in range(1, (n//2) + 2):
        if n%i == 0:
            s += i
    return s == n
        

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(n):
        num = int(input())
        perfect = is_perfect(num)
        if perfect:
            print("YES")
        else:
            print("NO")
    return 0

if __name__ == '__main__':
    main()