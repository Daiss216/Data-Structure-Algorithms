## Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates(self, nums):
        
        left= 1
        count= 1

        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
                count+= 1
            else:
                count=1

            if count <= 2:
                nums[left] = nums[r]
                left+=1

        return left