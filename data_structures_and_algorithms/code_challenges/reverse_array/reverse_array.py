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
    # Base Case : if we've reached the end of the array, break out bc we are done
    if i > pointer :
      break

    # hang on to that pointer's index
    place_holder = arr[pointer]

    # reassign the pointer's current index to the array's current iterator 
    arr[pointer] = arr[i]
    
    # the placeholder's index is assigned to the current index
    arr[i] = place_holder

    # move the pointer one index to the right
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
