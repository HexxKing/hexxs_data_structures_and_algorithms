# =========== FEATURED TASKS ============
# [X] - Write a function called reverse_array
# [X] - Takes an array as an argument
# [X] - Return an array with elements in reversed order
# [X] - Use a different technique


# Featured Technique - For Loop Iteration 
# Solution by Edwin Del Rio
def reverse_array(arr):
  # set a pointer to the end of the array
  pointer = len(arr) - 1

  for i in range(0, len(arr), 1):
    # Base Case : if we've reached the middle of the array, break out bc we are done iterating
    if i > pointer :
      break

    # hang on to the index at the pointer's value
    place_holder = arr[pointer]

    # This is where the swap happens
    # the pointer's index is reassigned to the current iteration's index
    arr[pointer] = arr[i]
    # the placeholder's value is assigned to the current iteration's index
    arr[i] = place_holder

    # reassign the pointer's index to move down the array one index to the left
    pointer -= 1
  return arr


# Alternative Technique - Slicing 
def reverse_array_sliced(arr):
  new_list = arr[::-1]
  return new_list


# Alternative Technique - Reverse() Built In Method
def reverse_array_built_in(arr):
  arr.reverse()
  return(arr)


# Alternative Technique - Reversed() Built In Method
def reversed_array_built_in(arr):
  return list(reversed(arr))

