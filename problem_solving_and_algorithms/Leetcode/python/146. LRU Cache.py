class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value  



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
