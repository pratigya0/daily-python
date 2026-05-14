#to count repeated leter in single word

'''word = input("Enter word: ")
count = {}

for char in word:
    if char in count:
        count[char] = count[char] + 1  # update count
    else:
        count[char] = 1                 # first time seen

for char, freq in count.items():
    print(f"{char} → {freq}")



# count words -- how many time its appear
sentence = "hello world hello python world"
count = {}

for word in sentence.split():
    if word in count:
        count[word] = count[word] + 1    
    else:
        count[word] = 1                 

for word, freq in count.items():   
    print(f"{word} → {freq}")'''


# 2 appears 3 times — most frequent!
numbers = [1, 2, 3, 2, 4, 2, 5, 3]
count = {}

for item in numbers:
    count[item] = count.get(item, 0) + 1

print(max(count, key=lambda x: count[x]))  # 2


