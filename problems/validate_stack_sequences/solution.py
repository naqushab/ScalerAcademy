class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = collections.deque()
        pos = 0
        for push in pushed:
            while st and st[-1] == popped[pos]:
                st.pop()
                pos += 1
            st.append(push)
        while st and st[-1] == popped[pos]:
            st.pop()
            pos += 1
        return len(st) == 0