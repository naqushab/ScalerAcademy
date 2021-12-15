from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        if not key:
            return False
        key = key.lower()
        head = self.root

        for letter in key:
            index = self.get_index(letter)
            if not head.children[index]:
                head.children[index] = TrieNode(ch=letter)
            head = head.children[index]
        head.is_end_word = True

    def search(self, key):
        if not key:
            return False
        head = self.root
        for letter in key:
            index = self.get_index(letter)
            if not head.children[index]:
                return False
            head = head.children[index]
        if head and head.is_end_word:
            return True
        return False

    def delete(self, key):
        pass
