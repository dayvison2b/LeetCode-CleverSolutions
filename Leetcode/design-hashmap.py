# https://leetcode.com/problems/design-hashmap/?envType=daily-question&envId=2023-10-04

class MyHashMap:

    def __init__(self):
        self.hashKey = []
        self.hashVal = []

    def put(self, key: int, value: int) -> None:
        if key not in self.hashKey:
            self.hashKey.append(key)
            self.hashVal.append(value)
        else:
            self.hashVal[self.hashKey.index(key)] = value
    def get(self, key: int) -> int:
        if key in self.hashKey:
            return self.hashVal[self.hashKey.index(key)]
        return -1
    def remove(self, key: int) -> None:
        if key in self.hashKey:
            idx = self.hashKey.index(key)
            self.hashKey.pop(idx)
            self.hashVal.pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)