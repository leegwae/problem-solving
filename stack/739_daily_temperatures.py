from typing import List

class Solution:
    # n ^ 2
    # Time limit Exceeded
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     if len(temperatures) == 1:
    #         return [0]
    #
    #     answer = []
    #
    #     for i, temperature in enumerate(temperatures[:-1]):
    #         count = 0
    #         for j, next_temperature in enumerate(temperatures[i+1:]):
    #             if temperature < next_temperature:
    #                 count = (j + 1)
    #                 break;
    #         answer.append(count)
    #
    #     return answer + [0]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            print(i, cur, stack)
            while stack and cur > temperatures[stack[-1]]:
                lastIndex = stack.pop()
                answer[lastIndex] = i - lastIndex

            stack.append(i)

        return answer

if __name__ == '__main__':
    s = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    answer = s.dailyTemperatures(temperatures)
    print(answer)