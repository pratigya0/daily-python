from array import *
arr = array('i',[])

n = int(input("Enter the lenght of the array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)
print(arr)