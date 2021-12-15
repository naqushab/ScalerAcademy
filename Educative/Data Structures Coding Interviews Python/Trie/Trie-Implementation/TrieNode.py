class TrieNode:
    def __init__(self, ch=''):
        self.char = ch
        self.children = [None]*26
        self.is_end_word = False
