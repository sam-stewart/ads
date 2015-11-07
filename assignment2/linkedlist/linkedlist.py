class LinkedList(object):
    """ A simple singly linked list supporting append, first, last and reverse
    operations. The primary objective is to write a reverse method """

    class _Node(object):
        """ Lightweight class storing a single linked list node """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """ Creates an empty linked list """
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __iter__(self):
        walk = self._head
        while walk:
            yield walk._element
            walk = walk._next

    def append(self, e):
        """ Append a new element to the end of the linked list """
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            self._tail = new
        self._size += 1

    def last(self):
        """ Return the last item in the linked list """
        if self.is_empty():
            raise ValueError('List is empty')
        return self._tail._element

    def first(self):
        """ Return the first item in the linked list """
        if self.is_empty():
            raise ValueError('List is empty')
        return self._head._element

    def pop(self):
        """ Removes and returns the last element in the linked list """
        if self.is_empty():
            raise ValueError('List is empty')
        e = self._tail._element
        if len(self) == 1:
            self._tail, self._head = None, None
        else:
            walk = self._head
            while walk._next != self._tail:
                walk = walk._next
            self._tail = walk
            self._tail._next = None
        self._size -= 1
        return e

    def reverse(self):
        """ Reverse the linked list """
        walk = self._head
        prev = None
        while (walk):
            next = walk._next
            walk._next = prev
            prev = walk
            walk = next
        self._head, self._tail = self._tail, self._head
