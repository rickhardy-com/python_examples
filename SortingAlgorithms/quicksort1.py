#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:21:12 2022

@author: richardhardy
"""

array = [5,6,4,1,2, 3, 12,8]
def quicksort (array):
    print ('ARRAY LEN: ', len (array))
    while len(array) > 1:
        print ('Array: ', array)
        
        pointer = 0
        pivot = len(array) -1
        
        while pivot != pointer:
            
            if  pivot < pointer and array[pivot] > array[pointer] or pivot > pointer and array[pivot] < array[pointer]:
                
                pointer, pivot = pivot, pointer
                array[pivot], array[pointer] = array[pointer], array[pivot]
            
            if pointer > pivot:
                pointer -= 1      
            else:
                pointer += 1
            
            left_unsorted = array [0:pivot]
            right_unsorted = array [pivot+1:len(array)]
            
            
            right_sorted = quicksort (right_unsorted)
            left_sorted = quicksort (left_unsorted)
        
      
        
            result = left_sorted + [array[pivot]] + right_sorted
            
        return (result)
    return (array)
    
result = quicksort(array)
print (result)
