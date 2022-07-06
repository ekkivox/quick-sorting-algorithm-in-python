def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return(quick_sort(items_lower) + [pivot] + quick_sort(items_greater))

''' QUICK_SORT ALGORITHM EXAMPLE
list = []
for i in range(11):
    import random
    i = random.randrange(0, 11)
    list.append(i)

print(quick_sort(list))
'''