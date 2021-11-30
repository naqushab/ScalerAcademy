def reverse(A, s, e):
    while s <= e:
        A[s], A[e] = A[e], A[s]
        s += 1
        e -= 1

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(map(int, input().split()[1:]))
    n = len(A)
    B = int(input())
    B = B%n
    reverse(A, 0, n-1)
    reverse(A, 0, B-1)
    reverse(A, B, n-1)
    for n in A:
        print(n, end=" ")

if __name__ == '__main__':
    main()