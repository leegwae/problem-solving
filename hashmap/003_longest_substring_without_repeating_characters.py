class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        max_len = start = 0

        for i, ch in enumerate(s):
            if ch in used and start <= used[ch]:
                start = used[ch] + 1
            else:
                max_len = max(max_len, i - start + 1)

            used[ch] = i

        return max_len


if __name__ == '__main__':
    sln = Solution()
    s = "tmmzuxt"
    print(sln.lengthOfLongestSubstring(s))