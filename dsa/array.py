from array import *
vals = array("i",[5, 2, 9, 8, 4, 2])
vals.reverse()   #to reverse
print(vals)

for i in range(5):     #to print one by one
    print(vals[i])

newArr = array(vals.typecode, (a for a in vals))   #created new array
print(newArr.append(9))   # add new number

for e in newArr:
    print(e)
