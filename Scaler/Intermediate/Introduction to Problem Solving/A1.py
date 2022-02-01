import math
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    if n == 2:
        print("YES")
        return 0
    if n%2 == 0:
        print("NO")
        return 0
    is_prime = True
    for i in range(3, math.floor(math.sqrt(n))+1, 2):
        if n%i == 0:
            is_prime = False
    if is_prime:
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == '__main__':
    main()