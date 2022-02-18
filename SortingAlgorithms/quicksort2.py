#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:21:12 2022

@author: richardhardy
"""

array = [5,6,1,2,4,3 ]
def quicksort (array):
    global local_vars
    while len(array) > 1:
        
        pointer = 0
        pivot = len(array) -1
        
        while pivot != pointer:
            
            PIVOT_ON_RIGHT = pivot < pointer
            PIVOT_VAL_GREATER_THAN_POINTER_VAL = array[pivot] > array[pointer]
            
            if PIVOT_ON_RIGHT and PIVOT_VAL_GREATER_THAN_POINTER_VAL or not ( PIVOT_ON_RIGHT or PIVOT_VAL_GREATER_THAN_POINTER_VAL):
            
            #if PIVOT_ON_RIGHT and PIVOT_VAL_GREATER_THAN_POINTER_VAL or not (PIVOT_ON_RIGHT and PIVOT_VAL_GREATER_THAN_POINTER_VAL):
            
            #if  pivot < pointer and array[pivot] > array[pointer] or pivot > pointer and array[pivot] < array[pointer]:
                
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
