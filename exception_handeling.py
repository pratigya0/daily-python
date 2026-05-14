#Write a code that —

#Takes two numbers from user
#Divides them
#Handles division by zero error

try:
    num1 = int(input("enter your first number:  "))
    num2 = int(input("enter your second number:  "))

    divide = (num1/num2)
    print(divide)

except ValueError:
    print("please give a valid number")
except ZeroDivisionError:
    print("Zero is not a valid value here")
finally:
    print("Program finished!")