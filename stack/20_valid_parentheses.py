from Stack import Stack

class Solution:
    # OPEN_BRACKETS = ['(', '{', '[']
    # CLOSE_BRACKETS = [')', '}', ']']
    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False
    #
    #     brackets = Stack()
    #
    #     for ch in s:
    #         if ch in self.OPEN_BRACKETS:
    #             brackets.push(ch)
    #         elif ch in self.CLOSE_BRACKETS:
    #             openBracket = brackets.pop()
    #             if openBracket is None\
    #                     or (ch == ')' and openBracket != '(') \
    #                     or (ch == '}' and openBracket != '{') \
    #                     or (ch == ']' and openBracket != '['):
    #                 return False
    #
    #     if brackets.pop() is not None:
    #         return False
    #
    #     return True

    BRACKET_TABLE = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    # using list method
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets = []
        for ch in s:
            if ch in self.BRACKET_TABLE.keys():
                open_brackets.append(ch)
            elif ch in self.BRACKET_TABLE.values():
                if not open_brackets or\
                        self.BRACKET_TABLE[open_brackets.pop()] != ch:
                    return False

        return len(open_brackets) == 0


if __name__ == '__main__':
    sln = Solution()
    brackets = '{[]}'
    print(sln.isValid(brackets))