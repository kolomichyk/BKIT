import pytest
from main import get_roots

def test_zero_root():
    assert (len(get_roots(4, 0, 3)) == 0)

def test_one_root():
    assert (get_roots(1, 1, 0) == [0])

def test_two_root():
    assert (get_roots(3, -5, -28) == [-2, 2])

def test_three_root():
    assert (get_roots(1, -9, 0) == [-3, 0, 3])

def test_four_root():
    assert (get_roots(1, -73, 576) == [-8, -3, 3, 8])