import ctypes
import random
from time import time

class DynamicArray(object):

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise IndexError('Pop from empty list')

        val = self._A[self._n-1]
        self._A[self._n-1] = None
        self._n -= 1
        if float(self._n)/self._capacity <= 0.25:
            self._resize(2 * self._n)
        return val

    def _resize(self, c):
        B = self._make_array(c)
        for k in range (self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

# Makes comparisons and switches as needed, progressively from the back of the array.
# Binary search to determine the index before switching improves speed significantly, especially on large sets.
class DynamicSortedArray(DynamicArray):

    def __init__(self):
        DynamicArray.__init__(self)

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        i = self._n
        while i > 0 and self._A[i-1] > obj:
            self._A[i] = self._A[i-1]
            i -= 1
        self._A[i] = obj
        self._n += 1

if __name__ == "__main__":

    for s in [10, 100, 1000, 10000]:
        ints = random.sample(range(s * 2), s)
        print 'Input Size: ' + str(s)
        da = DynamicSortedArray()
        start_time = time()
        for i in ints:
            da.append(i)
        end_time = time()
        print 'Time: ' + str(end_time - start_time)
