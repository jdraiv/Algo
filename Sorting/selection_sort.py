# coding=utf-8
# Selection sort algorithm written by Jdraiv

"""
Worst case performance =  О(n2)
Best case performance = О(n2)
Average case performance = О(n2)
"""

import unittest

test_array = [3, 4, 45, 1, 7, 0, 15, 11, 28, 13]
test_array_two = [64, 25, 12, 22, 11]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(selection_sort(test_array), [0, 1, 3, 4, 7, 11, 13, 15, 28, 45])


def selection_sort(l):
    for c, pos in enumerate(l):
        c_lowest = pos

        for element in range(c, len(l)):
            if l[element] < c_lowest:
                c_lowest = l[element]

        l.pop(l.index(c_lowest))
        l.insert(c, c_lowest)
    return l

if __name__ == '__main__':
    unittest.main()