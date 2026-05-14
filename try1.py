'''print("h")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator") '''

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even = []
#odd = []

'''for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"even: {even}")
print(f"odd: {odd}")'''

'''even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(f"even: {even}")
print(f"odd: {odd}")'''


for i in range(1, 6):

    for j in range(i):

        print("*", end=" ")

    print()