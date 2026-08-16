# Finding single no. from the array of nums that appear twice(XOR)
class Solution(object):
    def singleNumber(self, nums):
        ans = 0

        for i in nums:
            ans=  ans ^ i

        return ans

#x ^ x = 0