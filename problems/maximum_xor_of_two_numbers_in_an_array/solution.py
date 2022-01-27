class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, binary):
        cur = self.root
        for b in binary:
            cur = cur.children[int(b)]
    
    def search(self, binary):
        cur = self.root
        ans = 0
        for ch in binary:
            v = 1 - int(ch)
            if v in cur.children:
                ans = (ans << 1) | 1
                cur = cur.children[v]
            else:
                ans = ans << 1
                cur = cur.children[int(ch)]
        return ans

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = -math.inf
        trie = Trie()
        l = len(bin(max(nums))) -2 
        for n in nums:
            b = bin(n)[2:].zfill(l)
            trie.insert(b)
            ans = max(ans, trie.search(b))
        return ans