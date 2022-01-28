class Word:
    def __init__(self):
        self.children = collections.defaultdict(Word)
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = Word()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.is_end_word = True
    
    def search(self, word: str) -> bool:
        def dfs(word, cur):
            if not word:
                return cur.is_end_word
            if word[0] == '.':
                return any (dfs(word[1:], cur.children[ch]) for ch in cur.children)
            else:
                if word[0] in cur.children:
                    return dfs(word[1:], cur.children[word[0]])
                else:
                    return False
                    
        cur = self.root
        return dfs(word, cur)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)