from binarytree import BinaryTree


class ListBinaryTree(BinaryTree):

    def __init__(self):
        self._nodes = [None]
        self._max_index = None
        self._size = 0

    def add_root(self, element):
        """ Add the root element as root """
        if self._nodes[0] is not None: raise ValueError('Root exists')
        self._nodes[0] = element
        self._check_max_index(0)
        self._size += 1
        return 0

    def add_left(self, position, element):
        """ Add element as left child of position """
        self._validate(position)
        index = 2 * position + 1
        if self._nodes[index] is not None:
            raise ValueError('Left child exists')
        self._nodes[index] = element
        self._check_max_index(index)
        self._size += 1
        return index

    def add_right(self, position, element):
        """ Add element as right child of position """
        self._validate(position)
        index = 2 * position + 2
        if self._nodes[index] is not None:
            raise ValueError('Right child exists')
        self._nodes[index] = element
        self._check_max_index(index)
        self._size += 1
        return index

    def _add_none_types(self):
        """ Maintain list length of element in highest index * 2 + 2. Create
        a new list of None types, copy references from old list """
        new = [None] * (self._max_index * 2 + 2)
        for x in range(len(self._nodes)):
            if self._nodes[x] is not None:
                new[x] = self._nodes[x]
        self._nodes = new

    def _check_max_index(self, index):
        """ Check if the supplied index is higher than higest currently
        occupied index, if so, assign new value and expand array size """
        if index > self._max_index:
            self._max_index = index
            self._add_none_types()

    def _validate(self, position):
        if type(position) is not int:
            raise ValueError('Supplied position is not an integer')
        if self._nodes[position] is None:
            raise ValueError('Supplied position does not exist')

    def __len__(self):
        """ Return number of elements """
        return self._size

    def root(self):
        return self._nodes[0]

    def parent(self, position):
        self._validate(position)
        return self._nodes[(position - 1) / 2]

    def is_empty(self):
        pass

    def is_leaf(self, p):
        pass

    def children(self, position):
        pass
