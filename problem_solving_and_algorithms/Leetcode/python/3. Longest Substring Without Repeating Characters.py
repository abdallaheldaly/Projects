class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0 
        maxlen = 0
        lookup = {}
        
        for i, x in enumerate(s):
            if x in lookup and start <= lookup[x]:
                start = lookup[x] + 1
            else:
                maxlen = max (maxlen, i - start + 1)
            lookup[x] = i
        return maxlen