"""Implementations of some sorting"""
import random

def merge(a0, a1, a):
    # todo
    i0 = i1 = 0
    for i in range(len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0+= 1
        else:
            a[i] = a1[i1]
            i1 += 1

def merge_sort(a):
    # todo
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0,a1,a)
    return a

def _quick_sort(a, i, n):
    # todo
    if n <= 1:
        return
    x = a[i + random.randint(0,n-1)]
    p = i-1
    j = i
    q = i+n
    while j < q:
        if a[j] < x:
            p += 1
            a[j],a[p] = a[p],a[j]
            j += 1
        elif a[j] > x:
            q -= 1
            a[j],a[q] = a[q],a[j]
        else: #a[j] = x
            j += 1
    _quick_sort(a,i,p-i+1)
    _quick_sort(a,q,n-(q-i))

def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a

def binary_search(a,x):
    n = len(a)
    r = n - 1 # end
    s = 0  # start
    while s < r:
        mid = (s + r) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            r = mid - 1
        else:
            s = mid + 1
    if a[s] == x:
        return s
    else:
        return -1

def binary_search1(a, x):
    n = len(a)
    r = n - 1  # end
    s = 0  # start
    while s < r:
        mid = (s + r) // 2
        if x < a[mid].title or x == a[mid].title:
            r = mid
        else:
            s = mid + 1
    if a[s].title.startswith(x):
        return s
    else:
        return None

