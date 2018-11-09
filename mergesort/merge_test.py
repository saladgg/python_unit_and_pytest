import pytest
import mergesort


def test_func():
    arr = [50, 3, 11, 7]
    mergesort.mergeSort(arr)
    assert arr == [3, 7, 11, 50]
