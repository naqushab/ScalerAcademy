class TrieNode:
    def __init__(self, ch=''):
        self.char = ch
        self.children = [None]*26
        self.is_end_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def get_order(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        if not word:
            return False
        word = word.lower()
        head = self.root
        for ch in word:
            ch_index = self.get_order(ch)
            if not head.children[ch_index]:
                head.children[ch_index] = TrieNode(ch)
            head = head.children[ch_index]
        head.is_end_word = True 

    def search(self, word: str) -> bool:
        if not word:
            return
        head = self.root
        word = word.lower()
        for ch in word:
            ch_index = self.get_order(ch)
            if not head.children[ch_index]:
                return False
            head = head.children[ch_index]
        return head.is_end_word
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return
        head = self.root
        prefix = prefix.lower()
        for ch in prefix:
            ch_index = self.get_order(ch)
            if not head.children[ch_index]:
                return False
            head = head.children[ch_index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)