class Solution(object):
    def minBitFlips(self, start, goal):

        xor= start ^ goal
        ans= 0

        while xor > 0:
            ans += xor & 1
            xor >>= 1

        return ans

   