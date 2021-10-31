class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_num = max(map(abs, nums))
        max_bits = (int)(math.log(max_num, 2)) + 2
        
        list1 = [0 for i in range(max_bits)]
        for no in nums:
            pos = 0
            while (no != 0 and pos < max_bits):
                if (no & 1 != 0):
                    list1[pos] += 1
                no >>= 1
                pos += 1
        for i in range(max_bits):
            list1[i] %= 3
        pos = 0
        result = 0
        for i in range(max_bits):
            if (list1[i] != 0):
                result += (2 ** pos)
            pos += 1
        print (list1, max_bits)
        if (list1[max_bits - 1] == 1):
            result = -(2 ** max_bits - result)
        return (result)
    
    
