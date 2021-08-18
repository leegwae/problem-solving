# 리스트 사용하기
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortString = lambda x: ''.join(sorted(x))

        sorted_strs = sorted(strs, key=sortString)
        groups = []

        for str in sorted_strs:
              if len(groups) == 0:
                    groups.append([str])
              else:
                    last_index = len(groups)-1
                    if sortString(str) == sortString(groups[last_index][0]):
                          groups[last_index].append(str)
                    else:
                          groups.append([str])

        return groups

# 딕셔너리 사용하기
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        
        for str in strs:
            groups[''.join(sorted(str))].append(str)
            
        return list(groups.values())




      
# ================ 시간 제한 초과 ================
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        
        def isAnagramOf(origin: str, target: str) -> bool:
            if len(origin) == len(target):
                for ch in origin:
                    if origin.count(ch) != target.count(ch):
                        return False
                    
                return True
            else:
                return False
            
        i = 0
        while len(strs) != 0:
            origin = strs[0]
            groups.append([origin])
            
            for target in strs[1:]:
                if isAnagramOf(origin, target):
                    groups[i].append(target)
                    
            strs = [str for str in strs if str not in groups[i]]
            
            i += 1
            
        return groups
                    


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        
        i = 0
        while len(strs) != 0:
            origin = strs[0]
            groups.append([origin])
            
            for target in strs[1:]:
                if sorted(origin) == sorted(target):
                    groups[i].append(target)
                    
            strs = [str for str in strs if str not in groups[i]]
            
            i += 1
            
        return groups
                    
            
