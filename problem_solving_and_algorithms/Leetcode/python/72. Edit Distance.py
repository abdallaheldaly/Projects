class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        distances = range(len(word1) + 1)
        for i2, c2 in enumerate(word2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(word1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]