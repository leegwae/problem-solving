from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(prev, pos):
            if pos == len(digits):
                self.ans.append(prev)
                return

            for curr in self.dic[digits[pos]]:
                dfs(prev + curr, pos + 1)

        if not digits:
            return []

        dfs("", 0)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))
