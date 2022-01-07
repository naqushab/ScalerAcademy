class State:
    def __init__(self, point, word_index, visited):
        self.point = point
        self.word_index = word_index
        self.visited = visited

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        w = list(word)
        
        def search(i, j):
            st = collections.deque()
            st.append(State((i, j), 0, set()))
            while st:
                state = st.pop()
                
                if state.word_index == len(w)-1:
                    return True
                
                if state.point not in state.visited:
                    state.visited.add(state.point)
                
                for p in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = state.point[0]+p[0], state.point[1]+p[1]
                    if 0<=x<r and 0<=y<c and board[x][y] == w[state.word_index+1] and (x,y) not in state.visited:
                        st.append(State((x, y), state.word_index+1, state.visited.copy()))
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if search(i, j):
                        return True
        return False