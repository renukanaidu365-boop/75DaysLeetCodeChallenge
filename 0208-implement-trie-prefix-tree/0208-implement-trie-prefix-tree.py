class TrieNode:
    def __init__(self):
        # Use a dictionary to store children nodes: character -> TrieNode
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initializes the trie object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word 
        that has the prefix prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
