# factorial no. code

n = int(input("enter no:  "))
result = 1

for i in range (1, n+1):
    result = result * i

print(result)



n = int(input("Enter number: "))

if n < 0:
    print("non f")
elif n == 0:
    print("n")
else:
    result =  1
    for i in range(1, n+1):
        result = result * i
    print(result)