from arrayqueue import ArrayQueue


class Tree:
    """ ABC tree sutrcture """

    class Position:
        """ Abstraction representing location of a single element. """

        def element(self):
            """ Return element stored at this position """
            raise NotImplementedError('not implemented')

        def __eq__(self, other):
            """ Return true if other position represents same location """
            raise NotImplementedError('not implemented')

        def __ne__(self, other):
            """ Return true if other does not represent some location """
            return not (self == other)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        """ Generate an iteration of all positions using a traversal algorithm """
        return self.breadthfirst()

    def root(self):
        """ Return Position representing the tree's root, or none """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ Return position representing p's parent, or none if root """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ Return the number of children that Position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate an iteration of positions representing p's children """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ Return the total number of elements in the tree """
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """ Return true if Position p represents the root of the tree """
        return self.root() == p

    def is_leaf(self, p):
        """ return True if Position p does not have any children """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if the tree is empty """
        return len(self) == 0

    def depth(self, p):
        """ Return the number of levels seperating Position p from the root """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """ Return the height of the tree """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def _height2(self, p):
        """ Return the height of the subtree rooted at Position p """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def preorder(self):
        """ Preorder iteration """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """ Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def breadthfirst(self):
        """ Breadth first iteration of all tree positions """
        if not self.is_empty():
            fringe = ArrayQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
