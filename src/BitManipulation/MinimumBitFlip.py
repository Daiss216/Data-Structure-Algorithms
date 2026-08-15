#Minimum Bit Flips to Convert Number
class Solution(object):
    def minBitFlips(self, start, goal):

        xor= start ^ goal      # 1010 ^ 0111 -> 1101
        ans= 0

        while xor > 0:
            ans += xor & 1     
            xor >>= 1

        return ans

   