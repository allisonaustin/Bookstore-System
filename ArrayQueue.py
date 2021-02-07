import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        #n is the number of elements in a
        self.n = 0
        #j is the index of the first element in a
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        '''
            Resize the array
        '''

        #creating a new temprorary array to store values of a
        temp = self.new_array(max(1,2*self.n))

        # copying values from a to b
        for k in range(0,self.n):
            temp[k] = self.a[(self.j+k) % len(self.a)]

        # setting memory address of temporary array to a
        self.a = temp
        self.j = 0


    def add(self, x : np.object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        #checking if we are at max capacity for our array
        if self.n+1 > len(self.a):
            self.resize()

        self.a[(self.j+self.n) % len(self.a)] = x

        self.n += 1
        return True

    def remove(self) -> np.object :
        '''
            remove the first element in the queue
        '''
        if self.n == 0:
            raise IndexError()

        x = self.a[self.j]

        self.j = (self.j + 1) % len(self.a)
        self.n -= 1

        if len(self.a) >= 3*self.n:
            self.resize()

        return x


    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
