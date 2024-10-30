## Requirements
Given an input array consisting only of 0s, 1s, and 2s, sort the array in a single traversal. You are not allowed to use any built-in sorting functions provided by Python.

## Approach

### Provided Approach
The provided algorithm uses the Dutch National Flag problem strategy, which sorts the array in a single pass while maintaining the order of 1s. The algorithm employs three pointers:

1. **Low Pointer**: Tracks the position to place the next 0.
2. **Mid Pointer**: Scans through the array.
3. **High Pointer**: Tracks the position to place the next 2.

- **Steps:**
  1. Initialize `low`, `mid`, and `high` pointers.
  2. Traverse the array with the `mid` pointer:
     - If the current element is 0, swap it with the element at the `low` pointer and move both pointers forward.
     - If the current element is 1, just move the `mid` pointer forward.
     - If the current element is 2, swap it with the element at the `high` pointer and move the `high` pointer backward.
  3. Repeat until `mid` surpasses `high`.

- **Time Complexity:**
  - Each element is visited once: `O(n)`.

- **Space Complexity:**
  - Input space: `O(n)` for the list itself.
  - Auxiliary space: `O(1)` since no additional data structures are used.
  - Total: `O(n + 1) => O(n)`.

### Alternative Approach
An alternative approach could involve counting the occurrences of 0s, 1s, and 2s using a dictionary or array, then reconstructing the sorted array based on these counts. 

- **Steps:**
  1. Initialize counters for 0s, 1s, and 2s.
  2. Traverse the list to count occurrences.
  3. Construct a new sorted array based on the counts.

- **Time Complexity:**
  - Counting: `O(n)`.
  - Reconstructing: `O(n)`.
  - Total: `O(n + n) => O(n)`.

- **Space Complexity:**
  - Input space: `O(n)`.
  - Auxiliary space: `O(1)` (for counts).
  - Total: `O(n + 1) => O(n)`.

### Trade-off
The main trade-off between the two approaches lies in space usage. The in-place algorithm is more space-efficient, while the counting method could be simpler to implement but requires additional space for counting.
