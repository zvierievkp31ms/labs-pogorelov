class _ListNode: 
    def __init__(self, word, length):
        self.value = word
        self.array = [0]*length
        self.next = None

    def incrementFreq(self, key):
        self.array[key] += 1

class LinkedList:
    def __init__(self, length):
        self.head = None
        self.length = length
    
    def push(self, item):
        node = _ListNode(item, self.length)
        return node

    def getNode(self, item):
        return None
    
    def toObj(self):
        return {}