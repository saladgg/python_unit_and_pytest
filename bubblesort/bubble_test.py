import bubble
import pytest


def test_bubblesort():
    arr = [2, 14, 9, 5, 10]
    bubble.bubble_sort(arr)
    assert arr == [2, 5, 9, 10, 14]
