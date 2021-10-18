class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, L = [], len(nums)
        
        def backtrack(path, counter):
            
            if len(path) == L:
                res.append(path)
                
            else:
                for n in counter:
                    if counter[n] > 0:
                        counter[n] -= 1
                        
                        backtrack(path + [n], counter)
                        
                        counter[n] += 1
                        
        backtrack([], Counter(nums))
        return res

    def permuteUnique2(self, nums):
        if not nums:
            return []

        ret = [[]]
        for n in nums:
            ls = []
            for ar in ret:
                for i in range(len(ar) + 1):
                    ls.append(ar[ : i] + [n] + ar[i:])

                    if i < len(ar) and ar[i] == n:
                        break
            ret = ls
            
        return ret
