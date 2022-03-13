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
    
    #pivot = low  # set pivot to start index
    #pivot_value = arr[low]
    #pivot = low - 1
    pivot = low 
    
    right_pointer = high # + 1
    

    while (True):
        
        # Find leftmost element greater than
        # or equal to pivot
        #pivot += 1
        

          
        # Find rightmost element smaller than
        # or equal to pivot
        #right_pointer -= 1
        while (list_location[right_pointer] > list_location[pivot]):
            right_pointer -= 1
          
            
        # If right pointer has gone past left pointer then go back to main function
        if (pivot >= right_pointer):
            return right_pointer
        
        #print ('pivot, p1, p2: ', pivot_value, pivot, right_pointer, arr[pivot], arr[right_pointer], arr)
        
        print ('Exchange: ', list_location[pivot], list_location[right_pointer])
        list_location[pivot], list_location[right_pointer] = list_location[right_pointer], list_location[pivot]
        #print ('changed to : ', pivot_value, pivot, right_pointer, arr[pivot], arr[right_pointer], arr)
    

''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''


def quickSort(list_location, low, high):
    ''' pi is partitioning index, arr[p] is now at right place '''
    print ('QUICKSORT FUNCTION', low, high, list_location)
    if (low < high):
        

        pivot = find_pivot(list_location, low, high)
        print ('pivot is position :', pivot, list_location[pivot])
        
        
        #pivot = find_pivot(low, high)
        

		# Separately sort elements before and after the pivot
        quickSort(list_location, low, pivot) # Left side of pivot
        quickSort(list_location, pivot + 1, high) # Right Side of Pivot



# Driver code
array = [10, 7, 8, 9, 1, 5, 5] #declare the array (This is a python list)
array_length = len(array)
quickSort (array, 0, array_length - 1) #send a pointer to the list, the start index and end index
print("Sorted array:")
print (array)

# This code is contributed by shubhamsingh10
