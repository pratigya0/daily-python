scores = {
    "Pratigya": 85,
    "Rahul": 92,
    "Sneha": 78,
    "Amit": 95
}

item = list(scores.items( )) #convert to item 

'''sorted_scores = sorted(scores.items(), key = lambda x: x[1], reverse = True)

for name, scores in sorted_scores:
    print(f"{name}:{scores}")'''

for i in range(len(item)):
    for j in range(i+1, len(item)):
        if item[j][1] > item [i][1]:
            item[i], item[j] = item[j], item[i]

for name, score in item:
    print (f"{name} : {score}")