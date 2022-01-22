class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def rotate_lock(lock):
            locks = []
            for i in range(4):
                locks.append(lock[:i] + str( ( int(lock[i])+1+10 ) %10 ) + lock[i+1:])
                locks.append(lock[:i] + str( ( int(lock[i])-1+10 ) %10 ) + lock[i+1:])
            return locks
        
        q = collections.deque()
        q.append(("0000", 0))
        visit = set(deadends)
        if '0000' in visit:
            return -1
        while q:
            lock, step = q.popleft()
            if lock == target:
                return step
            for new_lock in rotate_lock(lock):
                if new_lock not in visit:
                    visit.add(new_lock)
                    q.append((new_lock, step+1))
        return -1