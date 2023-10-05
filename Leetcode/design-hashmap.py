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

class MyHashMap:

    def __init__(self):
        self.hash = []

    def put(self, key: int, value: int) -> None:
        for array in self.hash:
            if key == array[0]:
                array[1] = value
                return
        self.hash.append([key,value])

    def get(self, key: int) -> int:
        for array in self.hash:
            if key == array[0]:
                return array[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hash)):
            if key == self.hash[i][0]:
                self.hash.pop(i)
                return