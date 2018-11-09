import pytest
import merge


def test_merge():
    arr = [50, 3, 11, 7]
    merge.mergeSort(arr)
    assert arr == [3, 7, 11, 50]
