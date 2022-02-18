import ctypes

i = 5     # create int(5) instance, bind it to i
j = i     # bind j to the same int as i
j = 3     # create int(3) instance, bind it to j
print (i, j)   # i still bound to the int(5), j bound to the int(3)

print (hex(id(j)))
print (hex(id(i)))

z=int(hex(id(i)),base=16)  #this will convert the hexadecimal value into integer value
print (ctypes.cast(id(j),ctypes.py_object).value)
print (z)


i = [1,2,3]   # create the list instance, and bind it to i
j = i         # bind j to the same list as i
i[0] = 5      # change the first item of i
print (j )      # j is still bound to the same list as i
print (i )      # j is still bound to the same list as i
print (j[2])      # j is still bound to the same list as i
print (hex(id(j)))
print (hex(id(i)))

print (hex(id(i[0])))
print (hex(id(i[1])))
print (hex(id(i[2])))




