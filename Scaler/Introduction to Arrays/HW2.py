def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while t > 0:
        t-=1
        s = input().strip()
        a = []
        for n in s.split():
            a.append(int(n))
        a = a[1:]
        if len(a) < 2:
            print("-1")
        else:
            top = max(a)
            c = 0
            sec = float("-inf")
            for n in a:
                if n == top:
                    c += 1
                if n != top:
                    sec = max(n, sec)
            if c == len(a):
                print("-1")
            else:
                print(str(sec))
            

if __name__ == '__main__':
    main()