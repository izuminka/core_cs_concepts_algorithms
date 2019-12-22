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
