''' Python implementation of QuickSort using Hoare's partition scheme. '''

''' This function takes first element as pivot, and places
	all the elements smaller than the pivot on the left side
	and all the elements greater than the pivot on
	the right side. It returns the index of the last element
	on the smaller side '''


def find_pivot(list_location, low, high):
#def find_pivot(low, high):
    
    
    #print ('len', len(arr))
    #print ("PARTITION FUNCTION")
    
    pivot = low  # set pivot to start index
    #pivot_value = arr[low]
    #left_pointer = low - 1
    left_pointer = low - 1
    
    right_pointer = high + 1
    

    while (True):
        
        # Find leftmost element greater than
        # or equal to pivot
        left_pointer += 1
        
        
        #NEVER HAPPENS
        while (list_location[left_pointer] < list_location[pivot]): 
            left_pointer += 1
            print ("FIRING WHAT NEVER FIRES")
          
        # Find rightmost element smaller than
        # or equal to pivot
        right_pointer -= 1
        
        
        while (list_location[right_pointer] > list_location[pivot]):
            right_pointer -= 1
          
            
        # If right pointer has gone past left pointer then go back to main function
        if (left_pointer >= right_pointer):
            return right_pointer
        
        #print ('pivot, p1, p2: ', pivot_value, left_pointer, right_pointer, arr[left_pointer], arr[right_pointer], arr)
        
        print ('Exchange: ', list_location[left_pointer], list_location[right_pointer])
        list_location[left_pointer], list_location[right_pointer] = list_location[right_pointer], list_location[left_pointer]
        #print ('changed to : ', pivot_value, left_pointer, right_pointer, arr[left_pointer], arr[right_pointer], arr)
    

''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''


def quickSort(list_location, low, high):
    ''' pi is partitioning index, arr[p] is now at right place '''
    print ('QUICKSORT FUNCTION', list_location, low, high)
    if (low < high):
        

        pivot = find_pivot(list_location, low, high)
        print ('pivot is position :', pivot, list_location[pivot])
        
        
        #pivot = find_pivot(low, high)
        

		# Separately sort elements before and after the pivot
        quickSort(list_location, low, pivot) # Left side of pivot
        quickSort(list_location, pivot + 1, high) # Right Side of Pivot



# Driver code
array = [10, 7, 8, 9, 1, 5,5 ] #declare the array (This is a python list)
array_length = len(array)
quickSort (array, 0 , array_length - 1) #send a pointer to the list, the start index and end index
print("Sorted array:")
print (array)

# This code is contributed by shubhamsingh10
