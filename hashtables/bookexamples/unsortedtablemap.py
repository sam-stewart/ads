from mapbase import MapBase


class UnsortedTableMap(MapBase):
    """ Map implementation using an unordered list """

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        """ Return value associated with key k """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key not found')

    def __setitem__(self, k, v):
        """ Assign a value v to key k, overwiring existing val """
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """ Remove item associated with key k """
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key not found')

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key
