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
        if self.head == None:
            self.head = node
            return node
        
        buff = self.head
        if buff.value > item:
            node.next = buff
            self.head = node
            return node
        
        while buff.next:
            if buff.next.value > item:
                break
            buff = buff.next
        node.next = buff.next
        buff.next = node
        return node

    def getNode(self, item):
        buff = self.head
        while buff != None:
            if buff.value == item:
                return buff
            buff = buff.next
        return None
    
    def toObj(self):
        obj = {}
        buff = self.head
        while buff != None:
            obj[buff.value] = buff.array
            buff = buff.next
        return obj