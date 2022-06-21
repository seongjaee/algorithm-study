# 효율성 4,5 실패
def solution(words, queries):
    all_dict = {}
    for word in words:
        pre = ""
        suf = ""
        n = len(word)
        for idx, char in enumerate(word):
            pre += char
            pre_query = pre + "?" * (n - 1 - idx)
            all_dict[pre_query] = all_dict.get(pre_query, 0) + 1

            suf_query = "?" * (n - idx) + suf
            all_dict[suf_query] = all_dict.get(suf_query, 0) + 1
            suf = word[n - 1 - idx] + suf

    return [all_dict.get(q, 0) for q in queries]


# Trie
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}  # key: Node
        self.cnt = {}  # length: cnt


class Trie:
    def __init__(self):
        self.head = Node("")

    def insert(self, string):
        node = self.head
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
                node.children[char].cnt[len(string)] = 1
            else:
                node.children[char].cnt[len(string)] = (
                    node.children[char].cnt.get(len(string), 0) + 1
                )
            node = node.children[char]

    def search(self, string):
        node = self.head
        for char in string:
            if char == "?":
                break
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return node.cnt.get(len(string), 0)


class Suf_Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head
        node.cnt[len(string)] = node.cnt.get(len(string), 0) + 1

        for char in string[::-1]:
            if char not in node.children:
                node.children[char] = Node(char)
                node.children[char].cnt[len(string)] = 1
            else:
                node.children[char].cnt[len(string)] = (
                    node.children[char].cnt.get(len(string), 0) + 1
                )
            node = node.children[char]

        node.data = string

    def search(self, string):
        node = self.head
        for char in string[::-1]:
            if char == "?":
                break
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return node.cnt.get(len(string), 0)


def solution(words, queries):
    answer = []
    tree = Trie()
    suf_tree = Suf_Trie()
    for word in words:
        tree.insert(word)
        suf_tree.insert(word)
    for q in queries:
        if q[0] != "?":
            answer.append(tree.search(q))
        else:
            answer.append(suf_tree.search(q))

    return answer
