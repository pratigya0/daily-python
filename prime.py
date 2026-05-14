'''n = int(input("take a number:   "))

if n % 2 == 0 and n % 1 == 0:
    print("its a prime number")

else:
    print("invalid")'''


n = int(input("Enter a number: "))

if n <= 1:
    print("not a prime number")
else:
    for i in range (2, n):
        if n % i == 0:
            print(" its not a prime number")
        break
        
    else:
        print(" got prime")


n = int(input("Enter: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")



        

