class _DoublyLinkedBase(object):

    class _Node:
            # slots removes object's __dict__, saving memory.
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element   # wrapped element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """ Create new node, set predecessor's next to new node, and
        successor's previous to new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """ Delete node, point old previous at successor, and vice versa """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
