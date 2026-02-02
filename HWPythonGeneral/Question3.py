a = [1,2,3]
b = a[:] # Make this a deep copy
b[0] = 5
print (a)