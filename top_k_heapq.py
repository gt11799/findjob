#! /usr/bin/env python
'''
Top k element with heapq.
minimum k and maxmum k
'''

import heapq
import random

class MaxkHeap(object):
    '''
     Given k,
    return maxmum k elements, and sorted
    have two method: push and topk, just like heapq
    '''
    
    def __init__(self, k):
        self.k = k
        self.data = []
        
    def push(self, item):
        if len(self.data) < self.k:
            heapq.heappush(self.data, item)
        else:
            topk_small = self.data[0]
            if item > self.data[0]:
                heapq.heapreplace(self.data, item)
                
    def topk(self):
        '''
        return the maxmum sorted elements 
        '''
        return [item for item in reversed([heapq.heappop(self.data) for _ in xrange(len(self.data))])]
        
class MinkHeap(object):
    '''
    Given k
    return minimum k elements, and sorted
    have two method: push and topk.
    use a fabulous way to implement a topk minimum heap
    push -item, pop -item
    '''
    def __init__(self, k):
        self.k = k
        self.data = []
        
    def push(self, item):
        item = -item
        if len(self.data) < self.k:
            heapq.heappush(self.data, item)
        else:
            if item > self.data[0]:
                heapq.heapreplace(self.data, item)
                
    def topk(self):
        '''
        return minimum k sorted elements 
        '''
        return [-heapq.heappop(self.data) for _ in range(len(self.data))]
    
    
        
def test_topkHeap():
    list_sample = random.sample(xrange(1000), 100)
    topkheap_max = MaxkHeap(10)
    topkheap_min = MinkHeap(10)
    for item in list_sample:
        topkheap_max.push(item)
        topkheap_min.push(item)
    print("test Maxkheap when k=10: %s" %topkheap_max.topk())
    print("test Minkheap when k=10: %s" %topkheap_min.topk())
    
    
if __name__ == '__main__':
    test_topkHeap()