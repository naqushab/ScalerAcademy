class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nbrs = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nbrs[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        ans = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nbr in nbrs[pattern]:
                        if nbr not in visit:
                            visit.add(nbr)
                            q.append(nbr)
            ans += 1
        return 0