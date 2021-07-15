# set 사용하기
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = ['!', '?', '\'', ',', ';', '.']

        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')

        parsed = paragraph.split()
        edited = list(map(lambda x:x.lower(), parsed))

        keys = list(set(edited))
        keys = list(filter(lambda x: x not in banned, keys))

        temp = list(map(lambda x: (x, edited.count(x)), keys))
        temp.sort(key=lambda x: -x[1])
        
        return temp[0][0]


# collections.Counter() 사용하기
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = ['!', '?', '\'', ',', ';', '.']

        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')

        parsed = [word for word in paragraph.lower().split()
                  if word not in banned]
        
        counts = collections.Counter(parsed)

        return counts.most_common(1)[0][0]
        

        
        
        
        
                                 
        
        
        

        
        
                                 
        
        
        
