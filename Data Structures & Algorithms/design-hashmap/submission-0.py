class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        bucket = self.buckets[h]
        
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i][1] = value
                return
        
        bucket.append([key, value])

    def get(self, key: int) -> int:
        h = self._hash(key)
        bucket = self.buckets[h]
        
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
                
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        bucket = self.buckets[h]
        
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return