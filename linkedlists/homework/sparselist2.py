class SparseList(object):
    """ A sparesely populated array-like structure implemented as linked list.
    unpopulated fields default to zero. """

    class _Node:
        __slots__ = '_element', '_prev', '_next', '_index'

        def __init__(self, element, index, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            self._index = index

    def __init__(self, size):
        self._header = self._Node(None, -1, None, None)
        self._trailer = self._Node(None, size, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._SIZE = size

    def __len__(self):
        return self._SIZE

    def __iter__(self):
        index = 0
        while index < self._SIZE:  # Inefficient, getitem starts from head each call
            yield self.__getitem__(index)
            index += 1

    def __setitem__(self, index, element):
        if index < 0 or index > self._SIZE - 1:
            raise IndexError('Supplied index not within bounds')

        node = self._header
        while index > node._index:
            node = node._next

        if index == node._index:  # If index occupied, swap out the element
            node._element = element
        else:
            new = self._Node(element, index, node._prev, node)
            node._prev._next = new
            node._prev = new

    def __getitem__(self, index):
        if index < 0 or index > self._SIZE - 1:
            raise IndexError('Supplied index not within bounds')

        node = self._header
        while index > node._index:
            node = node._next

        return node._element if node._index == index else 0
