from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i, e in enumerate(target):
            if i == 0:
                continue
            if e <= target[i - 1]:
                ans = ans
            else:
                ans += e - target[i - 1]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumberOperations([1, 2, 3, 2, 1]))
