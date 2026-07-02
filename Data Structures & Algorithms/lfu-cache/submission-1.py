class LFUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.key_to_freq = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def touch(self, key):
        freq = self.key_to_freq[key]  # Get frequency of key from key_to_freq mapping
        del self.freq_map[freq][key]  # delete key from freq_map, as freq of key will be increased
        if not self.freq_map[freq]:   # check if freq_map is empty after above delete
            del self.freq_map[freq]   # if yes, delete freq entry from freq_map
            if self.min_freq == freq: # increment min_freq if its equal to freq
                self.min_freq += 1
        self.freq_map[freq + 1][key] = None # add key to respective maps
        self.key_to_freq[key] = freq + 1
    
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.touch(key)
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.touch(key)
            return
        
        if len(self.cache) == self.cap:
            evict_key, _ = self.freq_map[self.min_freq].popitem(last = False)
            del self.cache[evict_key]
            del self.key_to_freq[evict_key]

        self.cache[key] = value
        self.key_to_freq[key] = 1
        self.freq_map[1][key] = None
        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)