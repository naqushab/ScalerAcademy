class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()
        path_list = path.split('/')
        for item in path_list:
            if item == '':
                continue
            elif item == '/':
                if stack and stack[-1] == '/':
                    continue
                else:
                    stack.append('/')
            elif item == '.':
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        ans = '/'
        while stack:
            item = stack.pop()
            ans = '/' + item + ans
        if ans == '' or ans == '/':
            return '/'
        else:
            return ans[:-1] if ans[-1] == '/' else ans