# Algorithms

Algorithms are step-by-step formulas for solving problems and performing tasks. They are a set of rules or instructions that specify the sequence of operations to be performed to solve a particular problem.

Algorithms provide a systematic approach to problem-solving. The efficiency of an algorithm is often measured in terms of time and space complexity known as Big O. Different algorithms can be applied to solve the same problem, and their efficiency may vary.

## 📚 Implementation Roadmap

- **Sorting Algorithms**
  - Sorting algorithms are a set of techniques used to arrange elements in a specific order, typically in ascending or descending order based on some criteria. Sorting is a fundamental operation in computer science and plays a crucial role in various applications, including searching, data analysis, and database operations. 
  - Each sorting algorithm has its own strengths and weaknesses, and the choice of which to use depends on factors such as the size of the dataset, the distribution of data, and the available resources.
  - **Selection Sort** is a simple comparison-based sorting algorithm. It divides the input array into a sorted and an unsorted region. In each iteration, the smallest (or largest) element from the unsorted region is selected and swapped with the first element of the unsorted region.
  - **Insertion Sort** is another elementary sorting algorithm. It builds the sorted array one element at a time. It takes each element from the unsorted part of the array and inserts it into its correct position in the sorted region, shifting the other elements accordingly.
  <!-- - **Heap Sort** is a comparison-based sorting algorithm that uses a binary heap data structure. It first builds a max-heap (for ascending order) or a min-heap (for descending order). The root element (maximum or minimum) is then swapped with the last element in the array, and the heap property is restored. This process is repeated until the entire array is sorted. -->
  - **Bucket Sort** is a distribution sort algorithm that distributes elements into a finite number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or recursively applying the bucket sort. Finally, the sorted elements from all the buckets are concatenated to produce the sorted array.
  - **Radix Sort** is a non-comparative integer sorting algorithm that sorts numbers by processing individual digits. It can be applied to integers or strings of digits. The algorithm processes the digits from the least significant to the most significant (or vice versa), using a stable sort for each pass.
  - **Counting Sort** is a non-comparative integer sorting algorithm that works by counting the number of occurrences of each element and using those counts to reconstruct the sorted array. It assumes that the input elements are integers within a specific range.
  - **Shell Sort** is an optimization of Insertion Sort that works by comparing elements separated by a certain gap and gradually reducing the gap. The last iteration of Shell Sort is a regular Insertion Sort with a gap of 1, ensuring that the array is almost sorted before the final pass.

<!-- - **Searching Algorithms**
  - Searching algorithms are methods or procedures used to find a particular item, value, or information in a collection of data. These algorithms are essential for efficiently locating elements in various data structures, such as arrays, lists, trees, graphs, and more. 
  - The choice of a searching algorithm depends on factors such as the nature of the data, whether it is sorted, and the specific requirements of the search operation.
  - **Linear Search**, also known as Sequential Search, is a simple search algorithm that looks through each element in a list or array sequentially until the target element is found or the end of the list is reached.
  - **Interpolation Search** is an improved variant of binary search for uniformly distributed datasets. It estimates the position of the target element based on its value and the values of the endpoints.
  - **Exponential Search** is a search algorithm designed for sorted arrays. It involves determining a range where the target element might be present and then performing a binary search within that range.
  - **Jump Search** is a search algorithm that works on sorted arrays. It divides the array into blocks and jumps through these blocks to find the range where the target element might be, followed by a linear search within that range.
  - **Fibonacci Search** is a search algorithm that applies binary search within a narrow range determined by Fibonacci numbers. It narrows down the search space by using Fibonacci numbers to define the size of the subarray.
  - **Ternary Search** is a divide-and-conquer search algorithm similar to binary search but divides the search space into three parts instead of two. It requires sorted data and searches for the target element by reducing the search space to one-third in each step. -->

<!-- - **Graph Algorithms**
  - Graph algorithms are a set of techniques and procedures designed to solve problems related to graphs. Graphs are mathematical structures that consist of nodes (vertices) and edges connecting these nodes. 
  - These algorithms are crucial for solving a wide range of problems related to graphs, and their applications extend to various domains, including computer networks, social networks, optimization, and logistics. The choice of a specific algorithm depends on the nature of the problem and the characteristics of the graph involved.
  - **Kruskal's Algorithm (Minimum Spanning Tree)** is a greedy algorithm that finds a minimum spanning tree for a connected, undirected graph. It starts with an empty tree and repeatedly adds the smallest edge that does not form a cycle with the edges already chosen.
  - **Dijkstra's Algorithm (Shortest Path)** is a greedy algorithm that finds the shortest path between two vertices in a weighted graph. It maintains a set of vertices whose shortest distance from the source is known and iteratively expands the set by adding the vertex with the smallest tentative distance.
  - **Floyd-Warshall Algorithm (All Pairs Shortest Path)** is a dynamic programming algorithm that finds the shortest paths between all pairs of vertices in a weighted, directed or undirected graph. It works by considering all possible intermediate vertices in each iteration.
  - **Topological Sort** is an ordering of the vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before v in the ordering. It is often used in task scheduling and dependency resolution.
  - **Prim's Algorithm (Minimum Spanning Tree)** is a greedy algorithm that finds a minimum spanning tree for a connected, undirected graph. It starts with an arbitrary vertex and repeatedly adds the smallest edge that connects a vertex in the tree to a vertex outside the tree.
  - **Bellman-Ford Algorithm (Single-Source Shortest Path)** is a dynamic programming algorithm that finds the shortest paths from a single source vertex to all other vertices in a weighted, directed graph. It handles graphs with negative weight edges and detects negative weight cycles.
  - **Tarjan's Algorithm (Strongly Connected Components)** is an algorithm for finding the strongly connected components (SCCs) of a directed graph. It uses depth-first search (DFS) to assign a unique number to each vertex and identifies SCCs based on these numbers.
  - **Ford-Fulkerson Algorithm (Max Flow)** is an iterative method for finding the maximum flow in a flow network. It uses augmenting paths to increase the flow from the source to the sink until no more augmenting paths can be found.
  - **Edmonds-Karp Algorithm (Max Flow with Ford-Fulkerson)** is a specific implementation of the Ford-Fulkerson Algorithm that uses breadth-first search (BFS) to find augmenting paths. It ensures a polynomial time complexity, making it suitable for practical applications.
  - **Johnson's Algorithm (All Pairs Shortest Paths with Negative Weights)** is a method for finding all pairs shortest paths in a graph, even if it contains negative weight edges. It involves modifying the edge weights, applying Dijkstra's Algorithm for each vertex, and then adjusting the results. -->

<!-- - **Dynamic Programming Algorithms**
  - Dynamic programming is a technique in computer science used to solve optimization problems by breaking them down into simpler overlapping subproblems and solving each subproblem only once, storing the solutions to subproblems to avoid redundant computations.
  - Dynamic programming algorithms are designed to efficiently solve problems that exhibit the property of optimal substructure, meaning that the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
  - These algorithms often involve constructing a table or array to store solutions to subproblems, and the solutions are built up from the bottom (the simplest subproblems) to the top (the original problem). Dynamic programming is a powerful technique for solving complex problems efficiently by avoiding redundant computations through the use of memoization or tabulation. 
  - **Longest Common Subsequence (LCS)** is the longest sequence of characters that appears in the same order in two strings. It is a dynamic programming problem commonly used in bioinformatics, text comparison, and version control systems.
  - **Knapsack Problem** involves selecting a subset of items with given weights and values to maximize the total value, subject to a constraint on the total weight. It has applications in resource allocation and optimization.
  - **Matrix Chain Multiplication** problem involves finding the most efficient way to multiply a given sequence of matrices to minimize the number of scalar multiplications needed. It has applications in optimization and computer graphics.
  - **Longest Increasing Subsequence (LIS)** is the longest subsequence of a given sequence such that all elements are in increasing order. It is used in various applications, including data analysis and optimization.
  - **Edit Distance** measures the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another. It is used in applications such as spell checking, DNA sequence analysis, and natural language processing.
  - **Coin Change Problem** involves finding the number of ways to make change for a given amount using a set of coin denominations. It is a classic dynamic programming problem with applications in finance and optimization.
  - **Maximum Subarray Sum** problem involves finding the contiguous subarray with the largest sum in a given array of numbers. It has applications in data analysis, finance, and signal processing.
  - **Travelling Salesman Problem (TSP)** is a classic optimization problem where the goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city. It has applications in logistics, transportation, and network design.
  - **Subset Sum Problem** involves determining whether there exists a subset of a given set of numbers that adds up to a specified target sum. It has applications in resource allocation and partitioning problems.
  - **Rod Cutting Problem** involves cutting a rod into pieces of different lengths to maximize the total value obtained by selling the pieces. It is a classic optimization problem with applications in manufacturing and resource management.
  - **Maximum Bipartite Matching** problem involves finding the maximum cardinality matching in a bipartite graph. It has applications in resource allocation and assignment problems.
  - **Word Break Problem** involves determining whether a given string can be segmented into space-separated words from a dictionary. It has applications in natural language processing and text processing. -->

<!-- - **Divide and Conquer Algorithms**
  - Divide and Conquer is a powerful algorithmic paradigm where a problem is divided into smaller subproblems, which are solved independently, and the solutions to the subproblems are combined to solve the original problem. This technique is often used to solve problems with optimal substructure, meaning that the optimal solution to the problem can be constructed from optimal solutions of its subproblems.
  - The divide-and-conquer paradigm is often accompanied by a "conquer" step, where the solutions to the subproblems are combined to solve the original problem. 
  - **Strassen's Matrix Multiplication** is an algorithm for multiplying two matrices that reduces the number of multiplications from 8 to 7 by using a set of recursive formulas. It is based on the divide-and-conquer technique and is more efficient than the standard matrix multiplication algorithm for large matrices.
  - **Closest Pair of Points** algorithm finds the pair of points with the smallest Euclidean distance among a given set of points in the plane. It typically uses the divide-and-conquer approach to efficiently solve this problem.
  - **Karatsuba Algorithm (Fast Multiplication)** is a fast multiplication algorithm that recursively breaks down the multiplication of two numbers into three smaller multiplications. It reduces the number of required multiplications compared to the standard multiplication algorithm.
  - **Merge Sort** is a comparison-based sorting algorithm that uses the divide-and-conquer strategy. It divides the input array into two halves, recursively sorts them, and then merges the sorted halves to produce a sorted array.
  - **QuickSelect** is an algorithm for finding the kth smallest (or largest) element in an unordered list. It is based on the partitioning technique used in the QuickSort algorithm, making it a linear-time algorithm on average.
  - **Closest Pair of Points (2D and 3D)** algorithm extends to higher dimensions, such as 2D and 3D space. It aims to find the pair of points with the smallest Euclidean distance among a given set of points in the respective dimension.
  - **Fast Fourier Transform (FFT)** is an algorithm for efficiently computing the discrete Fourier transform (DFT) and its inverse. It is widely used in signal processing, image analysis, and many other applications to efficiently analyze and manipulate signals represented in the frequency domain.
  - **Maximum Subarray Sum in a Circular Array** algorithm finds the maximum sum of a subarray in a circular array. It involves considering both circular and non-circular subarrays and combines the results to find the overall maximum. -->

<!-- - **Greedy Algorithms**
  - Greedy algorithms are a class of algorithms that make locally optimal choices at each stage with the hope of finding a global optimum. At each step, a greedy algorithm selects the best available option without considering the consequences of that choice in the long run. The idea is to make the best immediate decision without worrying about future implications, with the assumption that the locally optimal choices will eventually lead to a globally optimal solution.
  - Greedy algorithms are often used for optimization problems where the goal is to find the best solution from a set of feasible solutions. They are particularly useful when the problem exhibits the greedy-choice property, meaning that a locally optimal choice is also globally optimal.
  - **Prim's Algorithm (Greedy for Minimum Spanning Tree)** is a greedy algorithm that finds a minimum spanning tree for a connected, undirected graph. It starts with an arbitrary vertex and grows the spanning tree by adding the smallest edge that connects a vertex in the tree to a vertex outside the tree.
  - **Kruskal's Algorithm (Greedy for Minimum Spanning Tree)** is a greedy algorithm that finds a minimum spanning tree for a connected, undirected graph. It starts with an empty set of edges and repeatedly adds the smallest edge that does not form a cycle with the edges already chosen.
  - **Dijkstra's Algorithm (Greedy for Shortest Path)** is a greedy algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph. It maintains a set of vertices whose shortest distance from the source is known and iteratively expands the set by adding the vertex with the smallest tentative distance.
  - **Huffman Coding (Optimal Prefix Codes)** is a greedy algorithm used for lossless data compression. It constructs an optimal prefix code for a set of characters based on their frequencies, with shorter codes assigned to more frequent characters.
  - **Fractional Knapsack Problem** involves selecting fractions of items with given weights and values to maximize the total value, subject to a constraint on the total weight. It is solved by selecting items based on their value-to-weight ratios in decreasing order.
  - **Job Scheduling (Greedy for minimizing completion time or maximizing profit)** algorithms aim to schedule a set of jobs with associated processing times or profits to optimize a certain criterion. Greedy approaches may prioritize jobs based on their processing time, profit, or other criteria to minimize completion time or maximize profit.
  - **Interval Scheduling** involves selecting a maximum-size subset of mutually non-overlapping intervals from a given set of intervals. Greedy algorithms can be employed to sort intervals based on their end times and select intervals greedily.
  - **Minimum Spanning Arborescence** is a spanning arborescence (directed tree) of minimum total edge weight in a directed graph. Algorithms like Chu–Liu/Edmonds' Algorithm are used to find this minimum spanning arborescence. -->

<!-- - **String Matching Algorithms**
  - String matching algorithms are techniques used to find the occurrence or occurrences of a specified pattern (substring) within a longer text (string). These algorithms are essential in various applications, including text processing, search engines, data mining, and bioinformatics.
  - The choice of a specific algorithm often depends on factors such as the size of the text, the length of the pattern, and the need for multiple pattern searches.
  - **Brute Force String Matching:** Compares the pattern to the text character by character, sliding the pattern one position at a time until a match is found or the end of the text is reached.
  - **Naive String Matching:** Similar to Brute Force, compares the pattern to the text character by character, sliding the pattern one position at a time.
  - **Rabin-Karp Algorithm:** Uses hashing to efficiently check if the pattern occurs in a window of characters in the text.
  - **Knuth-Morris-Pratt Algorithm:** Utilizes information about previous matches to avoid unnecessary character comparisons when a mismatch occurs.
  - **Boyer-Moore Algorithm:** Skips larger portions of the text when a mismatch occurs by precomputing a bad character heuristic and a good suffix heuristic.
  - **Aho-Corasick Algorithm (Multiple Pattern Matching):** Constructs a trie of patterns and efficiently searches for multiple patterns in the text simultaneously.
  - **Z Algorithm (Linear Time Pattern Searching):** Constructs the Z-array to efficiently find occurrences of a pattern in a text.
  - **Manacher's Algorithm (Longest Palindromic Substring):** Finds the longest palindromic substring in a given text using dynamic programming and symmetry properties. -->

<!-- - **Number-Theoretic Algorithms**
  - Number-theoretic algorithms are a class of algorithms that operate on integers and leverage properties and relationships from number theory to solve computational problems. 
  - They provide efficient solutions to problems related to integers and modular arithmetic, and they play a crucial role in the design and implementation of secure cryptographic systems.
  - **Euclidean Algorithm (GCD calculation):** Computes the greatest common divisor (GCD) of two integers using repeated application of the formula gcd(a, b) = gcd(b, a mod b). Used in finding the GCD is a fundamental operation in many number-theoretic and cryptographic algorithms.
  - **Sieve of Eratosthenes (Prime number generation):** Finds all prime numbers up to a given limit by iteratively marking the multiples of each prime. Used in primality testing and generating lists of primes for various applications.
  - **Extended Euclidean Algorithm (Finding modular inverses):** Computes the coefficients of Bézout's identity (ax + by = gcd(a, b)) along with the GCD of two integers. Used in modular inverse calculations and solving linear Diophantine equations.
  - **Chinese Remainder Theorem:** Solves systems of simultaneous modular congruences. Speeds up modular arithmetic and finds solutions to certain systems of linear congruences.
  - **Miller-Rabin Primality Test:** Probabilistic algorithm for primality testing based on modular exponentiation. Used in cryptographic applications and as a fast primality test.
  - **Pollard's rho Algorithm (Factorization):** A randomized algorithm for integer factorization. Used in factorizing large integers in number theory and cryptography. -->

<!-- - **Randomized Algorithms**
  - Randomized algorithms are algorithms that use randomness as part of their logic to make decisions or choices during their execution. Unlike deterministic algorithms, which produce the same output for a given input every time they run, randomized algorithms introduce an element of randomness, leading to different outcomes on different runs. The use of randomness is often employed to achieve certain desirable properties, such as improved efficiency or the ability to handle uncertainty.
  - Randomized algorithms are particularly useful in situations where deterministic algorithms might be impractical or inefficient. They are often applied in areas such as optimization, machine learning, cryptography, and distributed computing. The analysis of randomized algorithms typically involves assessing their expected performance over a range of possible random choices.
  - **Randomized QuickSort:** A variation of the QuickSort algorithm where the choice of the pivot element is randomized. Instead of selecting a fixed pivot, a random element from the array is chosen as the pivot during each partitioning step.
  - **Las Vegas Algorithms** are randomized algorithms that always produce the correct result, but their running time may vary due to the use of randomness. The algorithm continues executing until it finds the correct answer. Las Vegas algorithms are designed to guarantee correctness while allowing for variability in the runtime.
  - **Monte Carlo Algorithms** provide an answer that is probably correct. They use randomness to speed up the computation but may occasionally produce incorrect results. The probability of error can be controlled. Monte Carlo algorithms are particularly useful when an approximate solution is acceptable, and the focus is on achieving efficiency.
  - **Randomized Selection (Randomized QuickSelect):** A randomized algorithm for finding the k-th smallest element in an unsorted list. It is based on the same partitioning logic as QuickSort but focuses on only one side of the pivot based on the comparison with the desired element. Like Randomized QuickSort, the randomization in the selection process improves the average-case time complexity.
  - **Randomized Algorithms for Matrix Multiplication** use randomization to achieve faster average-case performance. These algorithms exploit the fact that, on average, certain random choices lead to more efficient matrix multiplication. The randomness in the algorithm allows for the avoidance of worst-case scenarios, improving the overall performance in practice. -->

<!-- - **Parallel Algorithms:**
  - **Parallel Merge Sort**: A parallelized version of the Merge Sort algorithm that exploits multiple processing units or threads to divide and conquer the sorting process. It involves recursively dividing the input data into smaller segments, sorting these segments independently in parallel, and then merging the sorted segments in a parallel manner to achieve a fully sorted array.
  - **Parallel QuickSort**: A parallelized version of the QuickSort algorithm that aims to sort elements concurrently by leveraging multiple processors or threads. It involves partitioning the array into segments that are independently sorted in parallel, followed by combining the sorted segments.
  - **Parallel Matrix Multiplication**: A method to multiply matrices by distributing the multiplication process across multiple processors or threads. It partitions the matrices into smaller submatrices and performs matrix multiplication concurrently on these submatrices.
  - **Parallel Breadth-First Search**: A parallelized version of the Breadth-First Search (BFS) algorithm used to explore nodes in a graph. It concurrently explores neighboring nodes of different vertices, potentially speeding up the traversal process by exploring multiple branches simultaneously.
  - **Parallel Depth-First Search**: A parallelized version of the Depth-First Search (DFS) algorithm used for graph traversal. It explores different branches of the graph concurrently by utilizing multiple processors or threads to search for paths from the starting vertex to other vertices.
  - **Parallel Prefix Sum (Scan)**: Calculates the prefix sum (also known as scan) of an array by dividing the array into segments and performing computations in parallel. It involves computing partial sums for segments concurrently and then combining these partial sums to obtain the final prefix sum. -->

<!-- - **Machine Learning Algorithms**
  - **K-Means Clustering**: An unsupervised machine learning algorithm used for clustering data points into k clusters based on similarity. It iteratively partitions the data into clusters by minimizing the sum of squared distances between data points and the centroid of their assigned cluster.
  - **Decision Trees**: A supervised learning algorithm used for classification and regression tasks. It builds a tree-like structure where each internal node represents a feature, each branch represents a decision based on that feature, and each leaf node represents a class label or regression value.
  - **Support Vector Machines**: A supervised learning algorithm used for classification and regression tasks. It finds the optimal hyperplane that best separates data points into different classes or predicts a continuous output by maximizing the margin between classes.
  - **Neural Networks (Backpropagation)**: A class of models inspired by biological neural networks used for supervised and unsupervised learning. Backpropagation is the primary algorithm used to train multilayer neural networks. It involves propagating errors backward through the network to adjust weights based on the gradient of the loss function.
  - **Random Forests**: An ensemble learning method that constructs multiple decision trees during training and outputs the mode or mean prediction of individual trees for classification or regression tasks. -->

<!-- - **Cryptography Algorithms**
  - **RSA Algorithm**: A public-key cryptosystem for secure communication and digital signatures. It involves the use of two keys: a public key used for encryption and a private key used for decryption. The security of RSA relies on the difficulty of factoring large composite numbers.
  - **Elliptic Curve Cryptography**: A public-key cryptography method based on the mathematical properties of elliptic curves over finite fields. ECC operates by leveraging the algebraic structure of elliptic curves for key generation, encryption, and digital signatures.
  - **Advanced Encryption Standard (AES)**: A symmetric-key encryption standard used to protect sensitive information. AES operates on fixed block sizes (128, 192, or 256 bits) and uses a series of substitution-permutation operations on data blocks with a secret key.
  - **Diffie-Hellman Key Exchange**: A method for securely exchanging cryptographic keys over an insecure channel. It enables two parties to establish a shared secret key without directly transmitting the key, using the concept of modular exponentiation and discrete logarithm problems. -->

## 📚 Solutions

<!-- category = data structures or code challenge -->
<!-- ## 🌟 Challenge Example Entry

  - [Challenge Description](./data_structures_and_algorithms/example_catagory/example_challenge/example_challenge_README.md) 
  - [Notes](./notes/example_challenge_notes.md)
  - [Whiteboard](./whiteboards/example_whiteboard.jpeg)
  - [Code Implementation](./data_structures_and_algorithms/example_catagory/example_challenge/example_challenge.py)
  - [Tests](./tests/test_example_challenge.py) -->