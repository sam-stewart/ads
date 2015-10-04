from priorityqueue import PriorityQueue
import math
from cStringIO import StringIO

def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
            if row != last_row:
                output.write('\n')
                columns = 2**row
                col_width = int(math.floor((total_width * 1.0) / columns))
                output.write(str(n).center(col_width, fill))
                last_row = row
                print output.getvalue()
                print '-' * total_width
                print
                return

pq = PriorityQueue()

pq.add(5, "Sam")
pq.add(23, "Sam")
pq.add(3, "Sam")
pq.add(45, "Sam")

print pq.remove_min()
print pq.remove_min()
print pq.remove_min()
print pq.remove_min()
