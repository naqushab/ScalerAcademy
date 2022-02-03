from collections import deque

def decode_string(s):
    ans = ''
    st = deque()
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num*10 + int(ch)
        elif ch == '[':
            if num > 0:
                st.append(str(num))
                num = 0
            else:
                st.append(str(1))
        elif ch.isalpha():
            st.append(ch)
        elif ch == ']':
            temp = ''
            while len(st) > 0:
                if st[-1].isalpha():
                    temp += st.pop()
                elif st[-1].isdigit():
                    st.append(temp*int(st.pop()))
                    break
    ans = ''
    while st:
        ans += st.pop()
    return ans[::-1]

def main():
    assert decode_string(s='3[ab2[c]]') == 'abccabccabcc'
    assert decode_string(s='3[ab2[c]]d') == 'abccabccabccd'
    assert decode_string(s='3[abc]2[d]') == 'abcabcabcdd'
    assert decode_string(s='abc2[d]') == 'abcdd'
    assert decode_string(s='3[abc]') == 'abcabcabc'
    assert decode_string(s='13[ab[c[d]]]') == 'abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd'


main()