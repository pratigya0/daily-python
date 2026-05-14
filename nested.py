nested = [1, [2, 3], [4, 5], 7]
result = []

for item in nested:
    if type(item) == list:
        result.extend(item)
    else:
        result.append(item)

print(result)  # [1, 2, 3, 4, 5, 7]