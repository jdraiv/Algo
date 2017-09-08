import unittest

# Bubble sort algorithm written by Jdraiv.

test_array_two = [5, 1000, 1200, 10, 100, 800]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bubble_sort(test_array_two), [5, 10, 100, 800, 1000, 1200])

def bubble_sort(list):
    c_sorting = True
    while c_sorting:
        c_sorting = False
        for pos, element in enumerate(list):
            if pos < len(list) - 1:
                if list[pos + 1] < element:
                    c_sorting = True
                    list[pos] = list[pos + 1]
                    list[pos + 1] = element
    return list

if __name__ == '__main__':
    unittest.main()