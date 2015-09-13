from listbinarytree import ListBinaryTree

tree = ListBinaryTree()

tree.add_root(5)
tree.add_left(0, 4)
p = tree.add_right(0, 7)
tree.add_left(p, 4)
p = tree.add_right(p, 7)
tree.add_left(p, 6)
tree.add_right(p, 12)

print "node list len: " + str(len(tree._nodes))
print "tree length: " + str(len(tree))

for x in tree._nodes:
    print x
