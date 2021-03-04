# =========== FEATURED TASKS ============
# [ ] - Write a function called reverse_array
# [ ] - Takes an array as an argument
# [ ] - Return an array with elements in reversed order
# [X] - Use a different technique


def reverse_array():
  pass


# Alternative Technique - Slicing 
def reverse_array_sliced(arr):
  new_list = arr[::-1]
  return new_list


# Alternative Technique - Reverse() Built In Method
def reverse_array_built_in(arr):
  arr.reverse()
  return(arr)
