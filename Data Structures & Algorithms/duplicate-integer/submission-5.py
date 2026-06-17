class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # l = len(nums)
        # for i in range (0,l-1,1) :
        #     for j in range (i+1,l,1):
        #         if nums[i] == nums[j]:
        #             return True
        #         # else: return False
        # return False

        seen = []
        for i in nums:
            if i in seen:
                return True
            seen.append(i)
        return False

