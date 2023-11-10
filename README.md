![header img](./assets/header.png)

<p align="center">
<a href="https://www.linkedin.com/in/hexx-king/" target="_blank" rel="noopener noreferrer"><img height="38" src="./assets/linkedin.png"></a>&nbsp;&nbsp;
<a href="mailto:hexxking13@gmail.com" target="_blank" rel="noopener noreferrer"><img height="35" src="./assets/gmail.png"></a>&nbsp;&nbsp;
</p> 

## Data Structures

Data structures are a way of organizing and storing data to perform operations efficiently. They define how data is stored, accessed, and manipulated.

Data structures provide a way to manage and organize data to meet the specific requirements of different algorithms. Choosing the right data structure is important for optimizing the performance of algorithms.

### Implementation Roadmap

- **Arrays:** A collection of elements, each identified by an index or a key.
  - Operations:
    - Access (read/write) an element by index.
    - Search for an element.
    - Insert an element at a specific index.
    - Delete an element from a specific index.

- **Sets:** A collection of distinct elements.
  - Operations:
    - Insert an element.
    - Delete an element.
    - Check if an element is present.
    - Perform set operations (union, intersection, difference).

- **Disjoint Set (Union-Find):** A data structure that keeps track of a set of elements partitioned into disjoint sets.
  - Operations:
    - Create a new set with element x.
    - Merge the sets containing elements x and y.
    - Determine the set to which element x belongs.
    - Path compression and union-by-rank are often used for optimization.

- **Linked Lists:** A sequence of elements where each element points to the next one in the sequence.
  - Operations:
    - Traverse the list.
    - Insert an element at the beginning, end, or a specific position.
    - Delete an element from the beginning, end, or a specific position.
    - Search for an element.

- **Skip List:** A data structure that allows fast search, insertion, and deletion of elements from a sorted sequence.
  - Operations:
    - Find the node with key x.
    - Insert a new node with key x.
    - Remove the node with key x.
    - Perform operations within a specific range efficiently.

- **Stacks:** A Last In, First Out (LIFO) structure where elements are added and removed from the same end.
  - Operations:
    - Push (add) an element onto the stack.
    - Pop (remove) the top element from the stack.
    - Peek (view) the top element without removing it.
    - Check if the stack is empty.

- **Queues:** A First In, First Out (FIFO) structure where elements are added at the rear and removed from the front.
  - Operations:
    - Enqueue (add) an element to the rear.
    - Dequeue (remove) an element from the front.
    - Peek (view) the front element without removing it.
    - Check if the queue is empty.

- **Deque (Double-ended Queue):** A queue where elements can be added or removed from both ends.
  - Operations:
    - Add element x to the front.
    - Add element x to the back.
    - Remove the element from the front.
    - Remove the element from the back.
    - Return the element at the front without removing it.
    - Return the element at the back without removing it.

- **Priority Queue:** An abstract data type similar to a regular queue or stack, but each element has an associated priority.
  - Operations:
    - Add element x to the priority queue.
    - Remove and return the minimum (or maximum) element.
    - Return the minimum (or maximum) element without removing it.
    - Ensure the heap property is maintained after an operation.

- **Trees:**
  - **Binary Trees:** Each node has at most two children.
  - **Binary Search Trees (BST):** A binary tree where the left child is less than or equal to the parent, and the right child is greater.
    - Operations:
      - Traverse the tree (in-order, pre-order, post-order).
      - Search for a specific node.
      - Insert a new node.
      - Delete a node.
      - Find the height or depth of the tree.

- **Trie:** A tree-like structure used to store a dynamic set or associative array where the keys are strings.
  - Operations:
    - Insert a word.
    - Search for a word.
    - Delete a word.
    - Autocomplete suggestions.

- **Hash Tables:** A data structure that implements an associative array abstract data type, where keys are mapped to values.
  - Operations:
    - Insert a key-value pair.
    - Delete a key-value pair.
    - Search for a value given a key.
    - Handle collisions (e.g., using chaining or open addressing).

- **Hash Maps:** Similar to hash tables, providing key-value mappings.
  - Operations:
    - Add a key-value pair to the map.
    - Remove a key-value pair based on the key.
    - Retrieve the value associated with a given key.
    - Manage situations where two keys hash to the same location.

- **Graphs:**
  - **Directed Graphs:** Edges have a direction.
  - **Undirected Graphs:** Edges have no direction.
  - **Weighted Graphs:** Edges have weights.
    - Operations:
      - Traverse the graph (DFS, BFS).
      - Search for a specific node.
      - Insert a new node.
      - Delete a node.
      - Check if there is a path between two nodes.

- **Heaps:**
  - **Min Heap:** The value of each node is less than or equal to the values of its children.
  - **Max Heap:** The value of each node is greater than or equal to the values of its children.
    - Operations:
      - Insert an element.
      - Extract the minimum or maximum element.
      - Peek at the minimum or maximum element without removing it.
      - Heapify: Maintain the heap property.

- **Bloom Filter:** A space-efficient probabilistic data structure used to test whether an element is a member of a set.
  - Operations
    - Add element x to the filter.
    - Check if element x is in the filter (may have false positives).
    - Remove element x from the filter (note: not always supported).

## Algorithms

Algorithms are step-by-step formulas for solving problems and performing tasks. They are a set of rules or instructions that specify the sequence of operations to be performed to solve a particular problem.

Algorithms provide a systematic approach to problem-solving. The efficiency of an algorithm is often measured in terms of time and space complexity known as Big O. Different algorithms can be applied to solve the same problem, and their efficiency may vary.

   **Examples of Algorithms:**
   - Sorting algorithms (e.g., Bubble Sort, QuickSort, Merge Sort)
   - Searching algorithms (e.g., Binary Search)
   - Graph traversal algorithms (e.g., Depth-First Search, Breadth-First Search)
   - Dynamic programming algorithms (e.g., Fibonacci sequence)

## Code Challenges

Code challenges are problems or puzzles that require a solution through programming. They are often used as a means to practice and improve coding skills, problem-solving abilities, and algorithmic thinking.

Code challenges serve as a practical application of data structures and algorithms. They help programmers enhance their problem-solving skills, understand how to choose appropriate data structures, and optimize algorithms for efficient solutions.

   **Examples of Code Challenges:**
   - Solving problems on coding platforms like LeetCode, HackerRank, or CodeSignal.
   - Participating in coding competitions like ACM ICPC, Google Code Jam, or Codeforces.
   - Completing programming exercises in textbooks or online courses.

<!-- category = data structures or code challenge -->
<!-- ## 🌟 Challenge Example Entry

  - [Challenge Description](./data_structures_and_algorithms/example_catagory/example_challenge/example_challenge_README.md) 
  - [Notes](./notes/example_challenge_notes.md)
  - [Whiteboard](./whiteboards/example_whiteboard.jpeg)
  - [Code Implementation](./data_structures_and_algorithms/example_catagory/example_challenge/example_challenge.py)
  - [Tests](./tests/test_example_challenge.py) -->


## 🌟 Array Reverse

  - [Challenge Description](./data_structures_and_algorithms/code_challenges/reverse_array/reverse_array_README.md) 
  - [Notes](./notes/reverse_array_notes.md)
  - [Whiteboard](./whiteboards/reverse_array.jpeg)
  - [Code Implementation](./data_structures_and_algorithms/code_challenges/reverse_array/reverse_array.py)
  - [Tests](./tests/test_reverse_array.py)


## 🌟 Array Shift

  - [Challenge Description](./data_structures_and_algorithms/code_challenges/array_shift/array_shift_README.md) 
  - [Notes](./notes/array_shift_notes.md)
  - [Code Implementation](./data_structures_and_algorithms/code_challenges/array_shift/array_shift.py)
  - [Tests](./tests/test_array_shift.py)


## 🌟 Linked Lists 

  - [Challenge Description](./data_structures_and_algorithms/data_structures/linked_lists/linked_lists_README.md) 
  - [Notes](./notes/linked_lists_notes.md)
  - [Code Implementation](./data_structures_and_algorithms/data_structures/linked_lists/linked_lists.py)
  - [Tests](./tests/test_linked_lists.py)


## 🌟 Trees

  - [Challenge Description](./data_structures_and_algorithms/data_structures/trees/trees_README.md) 
  - [Notes](./notes/trees_notes.md)
  - [Code Implementation](./data_structures_and_algorithms/data_structures/trees/trees.py)
  - [Tests](./tests/test_trees.py)


## 🌟 Array Operations

  - [Challenge Description](./data_structures_and_algorithms/data_structures/array_operations/array_operations_README.md) 
  - [Notes](./notes/array_operations_notes.md)
  - [Whiteboard](./whiteboards/array_operations.jpeg)
  - [Code Implementation](./data_structures_and_algorithms/data_structures/array_operations/array_operations.py)
  - [Tests](./tests/test_array_operations.py)


## More Challenges coming soon...


## 📚 Resources

- Header from <a href="https://www.canva.com/">Canva</a>
- Social media favicons from <a href="https://icons8.com">Icons8</a>
- Emoji Gif from <a href="https://tenor.com/">Tenor</a>
- Emojis from <a href="https://emojipedia.org/">Emojipedia</a>
- [Big O CheatSheet, Whiteboard Guide and Github Merge Checklist](./resources.md)
