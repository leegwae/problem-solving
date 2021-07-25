s = "babad"

def isPalindrom(s:str) -> bool:
      return s == s[::-1]

def getSubStrings(s:str) -> list:
      subStrings = []
      for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                  subStrings.append(s[i:j])
      return subStrings

subStrings = getSubStrings(s)

palindrom_substrings = [substring for substring in subStrings if isPalindrom(substring)]
palindrom_substrings.sort(key=lambda x:-len(x))

print(palindrom_substrings[0])
