a = input("enter first word:  ")
b = input("enter second word:  ")

if len(a) != len(b):
    print(" not match")
elif sorted(a) == sorted(b):
    print("anagram")
else:
    print("nopee A")


#second prblm
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("correct")
else:
    print("nope")
