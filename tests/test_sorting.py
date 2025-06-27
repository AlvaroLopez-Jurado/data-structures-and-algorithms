import unittest
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.merge_sort  import merge_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.heap_sort import heap_sort
from algorithms.sorting.counting_sort import counting_sort
from algorithms.sorting.radix_sort import radix_sort
from algorithms.sorting.bucket_sort import bucket_sort
from algorithms.sorting.shell_sort import shell_sort



class TestQuickSort(unittest.TestCase):
    def test_unsorted_list(self):
        self.assertEqual(quick_sort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_duplicates(self):
        self.assertEqual(quick_sort([4, 1, 4, 2]), [1, 2, 4, 4])

class TestMergeSort(unittest.TestCase):
    def test_unsorted_list(self):
        self.assertEqual(merge_sort([5, 2, 4, 1]), [1, 2, 4, 5])

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 3, 2, 1]), [1, 2, 3, 3])

class TestBubbleSort(unittest.TestCase):
    def test_bubble(self):
        self.assertEqual(bubble_sort([5, 1, 4]), [1, 4, 5])

class TestInsertionSort(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])

class TestHeapSort(unittest.TestCase):
    def test_unsorted_input(self):
        arr = [4, 10, 3, 5, 1]
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))

    def test_reverse_input(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))

    def test_with_duplicates(self):
        arr = [4, 2, 4, 3, 2]
        self.assertEqual(heap_sort(arr.copy()), sorted(arr))


class TestCountingSort(unittest.TestCase):    
    def test_unsorted_input(self):
        arr = [7, 3, 1, 4, 2]
        self.assertEqual(counting_sort(arr.copy()), sorted(arr))

    def test_sorted_input(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(counting_sort(arr.copy()), sorted(arr))

    def test_with_duplicates(self):
        arr = [5, 3, 5, 2, 3]
        self.assertEqual(counting_sort(arr.copy()), sorted(arr))


class TestRadixSort(unittest.TestCase):
    def test_unsorted_input(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        self.assertEqual(radix_sort(arr.copy()), sorted(arr))

    def test_sorted_input(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(radix_sort(arr.copy()), sorted(arr))

    def test_with_duplicates(self):
        arr = [10, 20, 10, 30, 20]
        self.assertEqual(radix_sort(arr.copy()), sorted(arr))

class TestBucketSort(unittest.TestCase):
    def test_unsorted(self):
        arr = [0.78, 0.17, 0.39, 0.26, 0.72]
        self.assertEqual(bucket_sort(arr.copy()), sorted(arr))

    def test_with_integers(self):
        arr = [4, 2, 7, 1, 3]
        self.assertEqual(bucket_sort(arr.copy()), sorted(arr))

class TestShellSort(unittest.TestCase):
    def test_unsorted(self):
        arr = [8, 5, 3, 1, 9]
        self.assertEqual(shell_sort(arr.copy()), sorted(arr))

    def test_with_duplicates(self):
        arr = [4, 2, 4, 3, 2]
        self.assertEqual(shell_sort(arr.copy()), sorted(arr))