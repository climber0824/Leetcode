class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        n = len(nums)
        
        for i in range(n-3):
            for j in range(i+1, n-2):
                remain = target - nums[i] - nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    temp = nums[l] + nums[r]
                    if temp < remain:
                        l += 1
                    elif temp > remain:
                        r -= 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return list(res)
