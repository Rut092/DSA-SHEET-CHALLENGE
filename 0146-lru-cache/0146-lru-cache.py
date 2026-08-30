class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}

        self.dummy_tail = Node(-1)
        self.dummy_head = Node(-1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map: return -1
        value,node = self.map[key]

        node_prev = node.prev
        node_nxt = node.next
        node_prev.next = node_nxt
        node_nxt.prev = node_prev

        head_nxt = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = head_nxt
        head_nxt.prev = node

        return value

    def make_node(self,key):

        nxt = self.dummy_head.next
        prev = self.dummy_head
        new_node = Node(key)

        prev.next = new_node
        new_node.prev = prev
        new_node.next = nxt
        nxt.prev = new_node

        return new_node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            _ ,node = self.map[key]
            self.map[key] = [value,node]
            self.get(key)
            return

        if len(self.map)>=self.capacity:
            del_node_key = self.dummy_tail.prev.val

            prev_prev = self.dummy_tail.prev.prev
            self.dummy_tail.prev = prev_prev
            prev_prev.next = self.dummy_tail
            
            del self.map[del_node_key]
            node = self.make_node(key)
        else:
            node = self.make_node(key)

        self.map[key] = [value,node]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)