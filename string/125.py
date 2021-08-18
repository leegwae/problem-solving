import collections

# 덱 이용하기
def use_deque(s: str) -> bool:
      strs : Deque = collections.deque()

      for ch in s:
            if ch.isalnum():
                  strs.append(ch.lower())

      while len(strs) > 1:
            if strs.popleft() != strs.pop():
                  return False

      return True


# 슬라이싱 이용하기
def use_slice(s:str) -> bool:
      strs = ''
      for ch in s.lower():
            if ch.isalnum():
                  strs += ch

      return strs == strs[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = str()
        
        for char in s:
            if char.isalnum():
                temp += char.upper()
                
        return temp == temp[::-1]
