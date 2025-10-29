from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prev = list()
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            prev.append(sum)
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] == 0:
                left = prev[i]
                right = sum - prev[i]
                if left == right:
                    ans += 2
                elif abs(left - right) == 1:
                    ans += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.countValidSelections([1,0,2,0,3]))
