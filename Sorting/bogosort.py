
import random


def is_sorted(l):
    if sorted(l) == l:
        return True
    else:
        return False


def bogosort(l):
    for c, element in enumerate(l):
        random_pos = random.randint(0, len(l))
        l.pop(c)
        l.insert(random_pos, element)
    return l


def apply_bogosort(l):
    the_list = bogosort(l)

    while not is_sorted(the_list):
        the_list = bogosort(l)
        print("Not sorted")
    return the_list


test = [5, 1000, 1200, 10, 100, 800]
print(apply_bogosort(test))