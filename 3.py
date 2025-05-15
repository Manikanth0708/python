def most_frequent_element(lst):
    if not lst:
        return None
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_count = 0
    most_frequent = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = item
    return most_frequent


data = [1, 3, 2, 1, 4, 1, 3, 2, 3, 3]
print(most_frequent_element(data))  
