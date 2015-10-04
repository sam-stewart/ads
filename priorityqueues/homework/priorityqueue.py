import heapq


class PriorityQueue(object):
    """ A priority queue implementation wrapping Python's heapq module """

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self.heap = []

    def add(self, k, v):
        """ Insert an item with key k and value v into the queue """
        heapq.heappush(self.heap, self._Item(k, v))

    def min(self):
        """ Return tuple (k,v) of minimum item in heap, do not remove """
        return (self.heap[0]._key, self.heap[0]._value)

    def remove_min(self):
        item = heapq.heappop(self.heap)
        return (item._key, item._value)

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)
