''' Python implementation of QuickSort using Hoare's partition scheme. '''


''' The main function that implements QuickSort
arr --> Array to be sorted,
start_pointer --> Starting index,
end_pointer --> Ending index '''

''' This function takes first element as pivot, and places
	all the elements smaller than the pivot on the left side
	and all the elements greater than the pivot on
	the right side. It returns the index of the last element
	on the smaller side '''






def quickSort(list_location, start_pointer, end_pointer):

    if (start_pointer != end_pointer):      #if the list is only one long, stop 
    
          
          print ("------------------------------------------")      
          print ('QUICKSORTING LIST: ', list_location, ' FROM:', start_pointer, 'TO:',end_pointer, list_location [start_pointer:end_pointer+1])
          
          left_pointer = start_pointer # set left pointer to the start index
          right_pointer = end_pointer + 1 
          pivot_found = False
          
          while not pivot_found:
                      
              # Find rightmost element smaller than
              # or equal to pivot
              right_pointer -= 1
              while (list_location[right_pointer] > list_location[left_pointer]):
                  right_pointer -= 1
                
              # If right pointer has gone back past left pointer then go back to main function 
              # with the new pivot value       
              if (left_pointer >= right_pointer):
                  pivot_found = True # Pivot is the right pointer
                  
              # exchange the values 
              else:    
                  print ('Exchange: ', list_location[left_pointer], list_location[right_pointer])
                  list_location[left_pointer], list_location[right_pointer] = list_location[right_pointer], list_location[left_pointer]
                  #print ('changed to : ', pivot_value, left_pointer, right_pointer, arr[left_pointer], arr[right_pointer], arr)
          
          		# Separately sort elements before and after the pivot
          quickSort(list_location, left_pointer, right_pointer) # Left side of pivot
          quickSort(list_location, right_pointer + 1, end_pointer) # Right Side of Pivot





#__main__
array = [10, 7, 8, 9, 1, 5, 5, 8] #declare the array (This is a python list)
array_length = len(array)
quickSort (array, 0 , array_length - 1) #send a pointer to the list, the start index and end index
print("Sorted list:")
print (array)

# This code is contributed by shubhamsingh10


'''
Pseudo Code, Hoare scheme.
--------------------------
QuickSort (array, start_pointer, end_pointer)
    if array length > 1
        
        set left_pointer = start
        set right_pointer = end
        set pivot_found = False
        
        while not pivot_found
            
            while array value at right_pointer > array value at left_pointer
                decrement right pointer
            
            if left_pointer >= right pointer
                pivot_found = True
            
            else
                swap value at right_pointer for array value at left_pointer
                
        end while
        
    QuickSort (array, start_pointer, right_pointer)
    QuickSort (array, right_pointer+1, end_pointer)

'''
