class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = 1
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node("")

    def insert(self, string):
        node = self.head
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
            else:
                node.children[char].cnt += 1
            node = node.children[char]

    def search(self, string):
        node = self.head
        for i, char in enumerate(string):
            node = node.children[char]
            if node.cnt == 1:
                return i
        return i


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word) + 1

    return answer
