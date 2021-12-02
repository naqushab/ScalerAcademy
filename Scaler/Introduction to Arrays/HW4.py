def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while t > 0:
        t -= 1
        A = []
        n = input()
        A = input().strip().split()
        A = list(map(int, A))
        o = [x for x in A if x%2==1]
        e = [x for x in A if x%2==0]
        if len(o) > 0:
            for n in o[:-1]:
                print(n, end=" ")
            print(str(o[-1]) + " ")
        else:
            print()
        if len(e) > 0:
            for n in e[:-1]:
                print(n, end=" ")
            print(str(e[-1]) + " ")
        else:
            print()

if __name__ == '__main__':
    main()