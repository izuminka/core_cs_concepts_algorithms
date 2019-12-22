## Data Structures Implementation and Algorithms (C++/Python)
This repository contains C++/Python 3 code showcasing my knowledge
and implementation of core CS data structures and algorithms.

## Array

<details><summary>Implementation </summary><blockquote>
Implement a vector (mutable array with automatic resizing).
When you reach capacity, resize to double the size. When popping an
item, if size is 1/4 of capacity, resize to half
<br>
<details><summary> OOP </summary>

- **attributes**
  - size() - number of items
  - capacity() - number of items it can hold
  - is_empty()
- **methods**
  - at(index) - returns item at given index, blows up if index out of bounds
  - push(item)
  - insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
  - aprepend(item) - can use insert above at index 0
  - pop() - remove from end, return value
  - delete(index) - delete item at index, shifting all trailing elements left
  - remove(item) - looks for value and removes index holding it (even if in multiple places)
  - find(item) - looks for value and returns first index with that value, -1 if not found
  - resize(new_capacity), private method
</details>

<details><summary> Analysis </summary>

- **Time**
  - O(1) to add/remove at end
  - O(n) to insert/remove elsewhere
- **Space**
  - O(n)
</details>

</blockquote></details>




<details><summary>Algorithms</summary><blockquote>
<details><summary>Sorting</summary>

- Quick Sort
- Heap Sort
- Merge Sort
</details>

<details><summary>Search</summary>

- Binary Search
  - first occurring
  - last occurring
</details>

</blockquote></details>


<details><summary>Associated Problems</summary>

- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
- [Plus One](https://leetcode.com/problems/plus-one/)

</details>


## Other
- **stack**
- **queues**
- **linked_lists**
- **graphs**
- **hash_ds**
- **heaps**
- **trees**


 # Concepts
<details>
<summary>General</summary>

    Recursion
    Dynamic Programming
    Object-Oriented Programming
    Design Patterns
    Combinatorics (n choose k) & Probability
    NP, NP-Complete and Approximation Algorithms
    Caches
    Processes and Threads
    Testing
    Scheduling
    String searching & manipulations
    Tries
    Floating Point Numbers
    Unicode
    Endianness
    Networking

    System Design,
    Scalability,
    Data Handling (if you have 4+ years experience)
    Bitwise operations


</details>
