#! /usr/bin/env python
'''
quick sort 
and use the same way to find median and the least k elements
'''
import random

def quicksort(q):
    
    if len(q) <= 1:
        return q
    else:
        pivot = q[0]
        return quicksort([x for x in q[1:] if x < pivot]) + [pivot] +\
             quicksort([x for x in q[1:] if x >= pivot])
             
        
def min_k_elements_helper(q, k):
    '''
    find the minimum k elements in q
    not sorted
    '''
    if len(q) == k:
        return q
    elif len(q) > k:
        pivot = q[0]
        left_half = [x for x in q[1:] if x < pivot] + [pivot]
        right_half = [x for x in q[1:] if x >= pivot]
        if len(left_half) == k:
            return left_half
        elif len(left_half) > k:
            return min_k_elements_helper(left_half, k)
        else:
            return left_half + min_k_elements_helper(right_half, k - len(left_half))
    else:
        raise
        
def min_k_elements(q, k):
    '''
    find the minimum k elements in q, sorted
    '''
    return quicksort(min_k_elements_helper(q, k))
        
def min_k_element(q, k):
    '''
    find the minimum k element in q, only one element
    damn my English
    '''
    return max(min_k_elements_helper(q, k))
    
def median(q):
    '''
    find median with the way of quick sort
    '''
    length = len(q)
    if length <= 1:
        return q[0]
    elif length % 2:
        return min_k_element(q, int(length/2) + 1)
    else:
        #import pdb; pdb.set_trace()
        left_half = min_k_elements_helper(q, length/2 + 1)
        mid_1 = max(left_half)
        left_half.remove(mid_1)
        mid_2 = max(left_half)
        return (mid_1 + mid_2) / 2.0
        
def min_k_elements_with_heapq(q, k):
    '''
    return the minimum k elements with heapq,
    and this is the fastest way
    '''
    from top_k_heapq import MinkHeap
    heap_min = MinkHeap(k)
    for item in q:
        heap_min.push(item)
    return heap_min.topk()
                   

def test_qsort():
    list_sample = random.sample(range(100), 30)
    print 'original list: ', list_sample
    list_sample = quicksort(list_sample)
    print 'quick sorted: ', list_sample
    
    
def test_min_k():
    list_sample = range(100) * 2
    random.shuffle(list_sample)
    sample_count = [list_sample.count(idx) for idx in range(10)]
    print 'original list count: ', sample_count
    print 'test minimum k element: ', min_k_element(list_sample, 10)
    print 'test minimum k elements: ', min_k_elements(list_sample, 10)
    
def test_median():
    list_sample = range(15)
    random.shuffle(list_sample)
    print 'original sample: ', quicksort(list_sample)
    print 'test median(15 elements): ', median(list_sample)
    list_sample = range(15) * 2
    print 'original sample: ', quicksort(list_sample)
    print 'test median(30 elements): ', median(list_sample)
    
if __name__ == '__main__':
    #test_qsort()
    #test_min_k()
    test_median()