## Data Structures Implementation and Algorithms (C++/Python)
This repository contains C++/Python 3 code showcasing my knowledge
and implementation of core CS data structures and algorithms.

## Array

<details><summary><strong>Implementation</strong></summary><blockquote><br>
Implement a vector (mutable array with automatic resizing).
When you reach capacity, resize to double the size. When popping an
item, if size is 1/4 of capacity, resize to half
<br>
<br>
<details><summary><strong>OOP</strong></summary><br>

- **attributes**
  - size - number of items
  - capacity - number of items it can hold
  - is_empty
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

<details><summary><strong>Analysis</strong></summary>

| Access  | Search | Insert | Delete | | Space |
| :---:   | :---:  | :---:  | :---:  |-| :---: |
| O(1)    | O(n)   | O(n)   | O(n)   | | O(n)  |

</details>

</blockquote></details>


<details><summary><strong>Algorithms</strong></summary><blockquote><br>
<details><summary><strong>Sorting</strong></summary><br>

- Quick Sort
- Heap Sort
- Merge Sort
</details>

<details><summary><strong>Search</strong></summary><br>

- Binary Search
  - first occurring
  - last occurring
</details>

</blockquote></details>


<details><summary><strong>Associated Problems</strong></summary><br>

- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
- [Plus One](https://leetcode.com/problems/plus-one/)

</details>



## Linked List

<details><summary><strong>Implementation</strong></summary><blockquote><br>

[**Singly ll Python**](https://github.com/izuminka/ds_algorithms/blob/master/linked_lists/impl/python/singly_ll.py)
<br>
[**Doubly ll C++**](https://github.com/izuminka/ds_algorithms/blob/master/linked_lists/impl/c%2B%2B/doubly_ll.cpp)

<br>
<br>
<details><summary><strong>OOP</strong></summary><br>

- **methods**
  - at(index) - returns item at given index
  - insert(index, value) - insert value at index
  - delete(index) - delete item at index
  - reverse() - reverses the list
  - front() - get value of front item
  - push_front(value) - adds an item to the front of the list
  - pop_front() - remove front item and return its value
  - back() - get value of end item
  - push_back(value) - adds an item at the end
  - pop_back() - removes end item and returns its value
</details>

<details><summary><strong>Analysis</strong></summary>

| Access  | Search | Insert | Delete | | Space |
| :---:   | :---:  | :---:  | :---:  |-| :---: |
| O(n)    | O(n)   | O(1)   | O(1)   | | O(n)  |

</details>

</blockquote></details>


<details><summary><strong>Algorithms</strong></summary><br>

- Merge Sort
- Quick Sort
- Detect loop in a linked list
</details>



<details><summary><strong>Associated Problems</strong></summary><br>

- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

</details>

## Other
- **stack**
- **queues**
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
