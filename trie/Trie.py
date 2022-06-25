from typing import Optional, Dict


class TrieNode:
	def __init__(self, key: Optional[str]):
		self.key = key
		self.isTerminal = False
		self.children: Dict[str, TrieNode] = {}


class Trie:
	def __init__(self):
		self.root = TrieNode(None)

	def insert(self, word: str) -> None:
		node = self.root

		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode(char)
			node = node.children[char]

		node.isTerminal = True

	def search(self, word: str) -> bool:
		node = self.root

		for char in word:
			if char not in node.children:
				return False
			node = node.children[char]

		return node.isTerminal

	def startsWith(self, prefix: str) -> bool:
		node = self.root

		for char in prefix:
			if char not in node.children:
				return False
			node = node.children[char]

		return True


# if __name__ == '__main__':
# 	trie = Trie()
# 	print('insert(poem)')
# 	trie.insert('poem')
# 	print(f'poem이 트라이에 있나요: {trie.search("poem")}')
# 	print(f'poe가 트라이에 있나요: {trie.search("poe")}')
# 	print(f'poe로 시작하는 문자열이 트라이에 있나요: {trie.startsWith("poe")}')
# 	print('insert(poe)')
# 	trie.insert('poe')
# 	print(f'poe가 트라이에 있나요: {trie.search("poe")}')
