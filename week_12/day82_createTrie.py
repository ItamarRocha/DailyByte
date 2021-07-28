"""
This question is asked by Microsoft. Implement a trie class that supports insertion and search functionalities.
Note: You may assume only lowercase alphabetical characters will added to your trie.

Ex: Given the following operations on your trie…

Trie trie = new Trie()
trie.insert("programming");
trie.search("computer") // returns false.
trie.search("programming") // returns true.
"""
class Trie():
    def __init__(self):
        self.trie = {}
    
    def insert(self, string):
        cur = self.trie
        for el in string:
            if el not in cur:
                cur[el] = {}
            cur = cur[el]
        cur["end"] = True

    def search(self, string):
        cur = self.trie
        for el in string:
            if el not in cur:
                return False
            cur = cur[el]
        return "end" in cur

tr = Trie()
tr.insert("programming")
tr.insert("programmer")
print(tr.trie)
print(tr.search("computer")) # False
print(tr.search("programming")) # True
print(tr.search("program")) # False
print(tr.search("programmer")) # True