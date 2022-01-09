class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        m = {0 : (0, 1), 
             1: (-1, 0),
             2: (0, -1),
             3: (1, 0)
            }
        x = y = 0
        d = 0
        for ch in instructions:
            if ch == 'L':
                d = (d+1)%4
            elif ch == 'R':
                d = (d+3)%4
            else:
                dx, dy = m[d][0], m[d][1]
                x, y = x+dx, y+dy
        return (x==0 and y==0) or d!=0