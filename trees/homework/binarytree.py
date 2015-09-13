from tree import Tree


class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure """

    def left(self, p):
        """ Return a position representing p's left child """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ Return a Position representing P's right child """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """ Return a Position representing p's sibling (or none) """
        parent = self.parent(p)
        if parent is None:              # p is root
            return None                 # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self, p):
        """ Generate an iteration of positions representing p's children. """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
