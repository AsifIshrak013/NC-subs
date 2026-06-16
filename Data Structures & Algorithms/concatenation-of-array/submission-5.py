class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # a = len(nums)
        # ans = 2 * a * [None]
        # for i in range(a):
        #     ans[i] = nums[i]
        #     ans[i+a] = nums[i]

        a = len(nums)
        ans = [None]*2*a

        for i in range (len(ans)):
            ans[i] = nums[i%a]

        return ans