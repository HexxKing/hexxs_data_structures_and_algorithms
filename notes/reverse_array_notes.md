
<h3 align="center"><a href="../table_of_contents.md">👈 Back to Table of Contents</a></h3>

---------------------------------------

# ✍️ Notes for Reverse Array
- Arrays are called "lists" in Python

---
### Reverse() - Perferred Way
```
# The Syntax
list_name.reverse()
```
- The `reverse()` method reverses the sorting order of the elements and returns a reversed iterator object.
- Python list class comes with the default `reverse()` function that inverts the order of items in the given list. It doesn’t create a new list object instead straightway modifies the original copy.
- It is the most recommended way to transpose the list both from speed and performance perspective.
- It doesn’t take any argument.
- Does not return any value in python but reverse the given object from the list.
- Every list object in python has a method called reverse() that you can call a list object and it will reverse the list in place.
- This means we don’t need to create a new list to copy these elements to a new list but instead you can modify the original list.
- So this is very fast because it happens in a place and doesn’t take up any extra memory.
- It modifies the existing list.

---
### Reversed()
```
# The Syntax
reversed(sequence) -> reverse iterator
```
- The `reversed()` function in Python allows us to process the items in a sequence in reverse order. 
- It accepts a sequence and returns an iterator that accesses the given sequence in the reverse order.
```
# Example:
my_list = [1, 2, 4, 3, 5]
print(list(reversed(my_list)))

# Output
[5, 3, 4, 2, 1]
```
- If you need to access individual elements of a list in reverse order, it’s better to use reversed() method in Python.
```
# Example: 

# Countries Name List
countries = ['India', 'USA', 'China']

# Printing Elements in Reversed Order
for c in reversed(countries):
  print(c)

# Output
China
USA
India
  ```

---
### Slicing
```
# The Syntax
reversed_list = original_list[::-1]
```
- Using the slicing technique, a copy of the list is made and the list is not sorted in-place.  Creating a copy requires more space to hold all of the existing elements. This exhausts more memory.
- Slicing creates a shallow copy of the original list taking up more memory. As it creates a copy it requires more space to hold all the existing elements.
- The point to note here is that structure of the list is replicated and not the contained objects i.e elements in a list. Hence, the elements are not duplicated thus saving space. 
  - Also, only the references in the structure holding addresses of objects are updated. As mutability applies to the elements contained in a list. If the object is modified it will be reflected in other copies as well.
- Slicing is fast. But it is difficult to understand decreasing readability of code as you go through the code.
- Understanding the script which is written using slicing could be time-consuming and difficult to visualize. The syntax is complex and doesn’t give a clear picture of what it is doing.

---
### Iterative Loops


---------------------------------------

## 📚 Resources Used in Researching Reverse Array
- [GeeksforGeeks](https://www.geeksforgeeks.org/python-reversing-list/)
- [w3schools](https://www.w3schools.com/python/ref_list_reverse.asp)
- [Python Pool](https://www.pythonpool.com/python-reverse-list/)