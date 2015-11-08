class Stack(object):
    """ LIFO stack backed by a python list """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack empty')
        return self._data.pop()
