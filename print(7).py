nums = [1, 2, 3, 2, 4, 1, 5]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)


a = 0
b = 1
for i in range(10):    
    print(a)             
    next = a + b       
    a = b                
    b = next

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b
fib(12)