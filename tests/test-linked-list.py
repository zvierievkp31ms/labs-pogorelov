import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.node_list = node_list = LinkedList(3)
        node_list.push(3)
        node_list.push(1)
        node_list.push(2)
    
    def tearDown(self):
        pass
    
    def test_search(self):
        item = self.node_list.getNode(3)
        self.assertEqual(item.next, None)

    def test_increment(self):
        item = self.node_list.getNode(3)
        item.incrementFreq(0)
        self.assertEqual(item.array[0], 1)
    
    def test_convert_to_obj(self):
        item = self.node_list.getNode(3)
        item.incrementFreq(1)
        result = self.node_list.toObj()
        self.assertEqual(result[3], [0, 1, 0])

if __name__ == "__main__":
    unittest.main()