
'''
Select p, the last element
Select i, the first element

Counter variables
I: Index of smaller value
J: Loop variable

i = -1
j = 0

if j < p:
    swap i and j

'''


def quicksort(l):
    pivot = l[-1]
    i = -1
    for c, element in enumerate(l):
        if element <= pivot and c < len(l) - 1:
            i += 1
            to_swap = l[i]

            l[i] = element
            l[c] = to_swap
        elif c == len(l) - 1:
            last_swap = l[i + 1]

            l[i + 1] = pivot
            l[c] = last_swap
    return l

def apply_quicksort(l):
    sorted_array = quicksort(l)
    mean = len(sorted_array) // 2

    array_one = sorted_array[0:mean + 1]
    array_two = sorted_array[mean + 1:]

    return quicksort(array_one) + quicksort(array_two)


test = [10, 80, 30, 90, 40, 50, 70]

print(apply_quicksort(test))
