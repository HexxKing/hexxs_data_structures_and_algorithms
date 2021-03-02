# =========== FEATURED TASKS ============
# [ ] - Write a function called reverse_array
# [ ] - Takes an array as an argument
# [ ] - Return an array with elements in reversed order
# [X] - Use a different technique


def reverse_array():
  pass


# Alternative Technique - Slicing 
# a copy of the list is made and the list is not sorted in-place. Creating a copy requires more space to hold all of the existing elements. This exhausts more memory.
def reverse_array_sliced(arr):
  new_list = arr[::-1]
  return new_list


# Alternative Technique - Built In Method
def reverse_array_built_in(arr):
  arr.reverse()
  return(arr)
