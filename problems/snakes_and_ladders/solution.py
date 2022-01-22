class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        
        def get_pos(pos, n):
            r = pos//n
            if r%2 == 0:
                c = pos%n
            else:
                c = (n-1)-(pos%n)
            return r, c
        
        n = len(board)
        q = collections.deque()
        q.append((1, 0))
        visit = set()
        visit.add(1)
        
        while q:
            pos, step = q.popleft()
            r, c = get_pos(pos-1, n)
            if pos == n*n:
                return step
            
            for i in range(1,7):
                index = pos + i -1
                if index >= n*n:
                    continue
                r, c = get_pos(index, n)
                if board[r][c] != -1:
                    new_pos = board[r][c]
                else:
                    new_pos = pos + i
                if new_pos not in visit:
                    visit.add(new_pos)
                    q.append((new_pos, step+1))
        
        return -1