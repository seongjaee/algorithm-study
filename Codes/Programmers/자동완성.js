class Node {
  constructor(key) {
    this.key = key;
    this.cnt = 1;
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node("");
  }

  insert(string) {
    let node = this.head;
    for (let char of string) {
      if (Object.keys(node.children).includes(char)) {
        node.children[char].cnt++;
      } else {
        node.children[char] = new Node(char);
      }
      node = node.children[char];
    }
  }

  search(string) {
    let node = this.head;
    for (let i = 0; i < string.length; i++) {
      const char = string.charAt(i);
      node = node.children[char];
      if (node.cnt == 1) {
        return i;
      }
    }
    return string.length - 1;
  }
}

function solution(words) {
  var answer = 0;
  const trie = new Trie();
  words.forEach((word) => {
    trie.insert(word);
  });

  words.forEach((word) => {
    answer += trie.search(word) + 1;
  });

  return answer;
}
