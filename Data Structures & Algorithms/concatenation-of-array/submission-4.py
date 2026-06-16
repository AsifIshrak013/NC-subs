class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # a = len(nums)
        # ans = 2 * a * [None]
        # for i in range(a):
        #     ans[i] = nums[i]
        #     ans[i+a] = nums[i]

        n = len(nums)
        ans = [None]*2*n

        for i in range (2*n):
            ans[i] = nums[i%n]

        return ans