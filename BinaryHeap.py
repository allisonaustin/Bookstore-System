import numpy as np
from Interfaces import Queue



def left(i : int):
    # todo
    return int(2 * i + 1)

def right(i: int):
    # todo
    return int(2 * (i + 1))

def parent(i : int):
    # todo
    return int((i-1)//2)

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0 #number of elements in the heap

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        # todo
        temp = self.new_array(max(2*self.n,1))
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp

    def add(self, x : object):
        # todo
        if len(self.a) == self.n:
            self.resize()
        self.a[self.n] = x
        self.n += 1
        self.bubble_up(self.n-1)

    def bubble_up(self, i):
        # todo
        if i < 0 or i >= self.n:
            raise IndexError()
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i],self.a[p] = self.a[p],self.a[i]
            i = p
            p = parent(i)

    def remove(self):
        # todo
        if self.n == 0:
            raise IndexError()
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self.trickle_down(0)
        if 3*self.n < len(self.a):
            self.resize()
        return x

    def trickle_down(self, i):
        # todo
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]: # r is in bounds, r < a[i]
                l = left(i)
                if self.a[l] < self.a[r]:       # left < right
                    j = l
                else:                           # right < left
                    j = r
            else:                                  # r > a[i]
                l = left(i)
                if l < self.n and self.a[l] < self.a[i]:    # left is in bounds, l < a[i]
                    j = l
            if j >= 0:
                self.a[j],self.a[i] = self.a[i],self.a[j]
            i = j

    def find_min(self):
        if n == 0: raise IndexError()
        return a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += str(self.a[i])
            if i  < self.n-1:
                s += ","
        return s + "]"

