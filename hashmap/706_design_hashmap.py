class MyHashMap:

    def __init__(self):
        self.l = []

    def put(self, key: int, value: int) -> None:
        if not self.hasKey(key):
            for _ in range(len(self.l) - 1, key):
                self.l.append(-1)

        self.l[key] = value

    def get(self, key: int) -> int:
        if self.hasKey(key):
            return self.l[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.hasKey(key):
            self.l[key] = -1

    def hasKey(self, key: int) -> True:
        return (key + 1) <= len(self.l)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)