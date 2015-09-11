class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        """ Return element at front """
        if self.is_empty():
            raise Empty("Deque is empty")
        # Get element at head after sentinel
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """ Add element to front of deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
