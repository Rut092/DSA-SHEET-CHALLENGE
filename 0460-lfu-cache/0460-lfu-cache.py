class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self,node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
        self.size+=1
    
    def remove(self,node):
        p,n = node.prev,node.next
        p.next = n
        n.prev = p
        self.size-=1

    def pop_lru(self):
        if self.size == 0 : return None
        lru = self.tail.prev
        self.remove(lru)
        return lru

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = {}

    def _update_freq(self,node):
        old_freq = node.freq
        self.freq_map[old_freq].remove(node)

        if old_freq==self.min_freq and self.freq_map[old_freq].size==0:
            self.min_freq+=1

        node.freq+=1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLL()
        
        self.freq_map[node.freq].add(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_map: return -1

        node = self.key_map[key]
        self._update_freq(node)

        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity==0: return 

        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
            return
        
        if len(self.key_map)>= self.capacity:
            lru_node = self.freq_map[self.min_freq].pop_lru()
            del self.key_map[lru_node.key]

        new_node = Node(key,value)
        self.key_map[key] = new_node
        
        if 1 not in self.freq_map:
            self.freq_map[1] = DLL()
        
        self.freq_map[1].add(new_node)
        self.min_freq = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)