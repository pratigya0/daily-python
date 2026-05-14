'''numbers = [1, 2, 3, 4, 5]
a = sum(numbers)
b = a/len(numbers) 
print("sum ->", a)
print("Average ->", b)

#find longest word
#words = ["apple", "banana", "kiwi", "mango", "fig"]
words = ["apple", "banana", "kiwi", "mango", "fig"]
longest = ""
for word in words:
    if len(word) > len(longest):
        longest=word

print(longest)


numbers = [1, 2, 3, 2, 4, 1, 5]
my_numbers = set(numbers)
num = list(my_numbers)
print(num)

numbers1 = [1, 2, 3, 4, 5]
print(numbers1[::-1])

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
my_list1 = set(list1)
my_list2 = set(list2)

print(list(my_list1 & my_list2))


string = "pratigya"
my_string = set(string)
if len(string) != len(my_string):
    print("Duplicate exists")
else:
    print("its not")


a = 20
b = 10 


numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]

total = sum(range(1, 11))    # 1 to 10 sum
actual = sum(numbers)              # list sum

print(total - actual)          # difference = missing! 


numbers = [10, 20, 4, 45, 99, 45]
#second largest number
numbers.sort()
print(numbers[-2])'''


'''string = "Pratigya"
#output Vowels → 3, Consonants → 5
vowels_count = 0
consonants_count = 0

for letter in string:
    if letter in "aeiouAEIOU":
        vowels_count += 1       # vowel mila!
    else:
        consonants_count += 1    # consonant mila!

print(f"Vowels → {vowels_count}")
print(f"Consonants → {consonants_count}")'''


string = "Pratigya"
vowels = 0
# vowels count
for letters in string:
    if letters in "aeiou":
        vowels += 1

print(f"vowels -> {vowels}")


# palidrome
string = "madam"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Fibonacci 
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = b, a+b


n = int(input("Enter number: "))
if n % 2 == 0:
    print('prime number detected')
else:
    print("no prime")