import pytest
from python.code_challenges.reverse_array.reverse_array import reverse_array, reverse_array_built_in, reverse_array_sliced, reversed_array_built_in

#Test Connection 
def test_reverse_array_connection():
  # return reverse_array()
  arr = [1]
  expected = reverse_array(arr)
  actual = [1]
  assert expected == actual


# ========= “Happy Path” - Expected Outcome ==========
def test_happy_path():
  arr = [1, 2, 3, 4, 5, 6]
  expected = reverse_array(arr)
  actual = [6, 5, 4, 3, 2, 1]
  assert expected == actual


# =========== Edge Case ================
def test_negative_numbers():
  arr = [89, 2354, 3546, 23, 10, -923, 823, -12]
  expected = reverse_array(arr)
  actual = [-12, 823, -923, 10, 23, 3546, 2354, 89]
  assert expected == actual


def test_large_collection():
  arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
  expected = reverse_array(arr)
  actual = [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
  assert expected == actual


# =========== Expected Failure ==============
def test_expected_failure():
  arr = []
  expected = reverse_array(arr)
  actual = []
  assert expected == actual


# ====== Alternative Technique - Slicing ======
def test_happy_path_sliced():
  arr = [1, 2, 3, 4, 5, 6]
  expected = reverse_array_sliced(arr)
  actual = [6, 5, 4, 3, 2, 1]
  assert expected == actual


# ====== Alternative Technique - Built In Method reverse() ======
def test_built_in_reverse_happy_path():
  arr = [1, 2, 3, 4, 5, 6]
  expected = reverse_array_built_in(arr)
  actual = [6, 5, 4, 3, 2, 1]
  assert expected == actual

# ====== Alternative Technique - Built In Method reversed() ======
def test_built_in_reversed_happy_path():
  arr = [1, 2, 3, 4, 5, 6]
  expected = reversed_array_built_in(arr)
  actual = [6, 5, 4, 3, 2, 1]
  assert expected == actual
