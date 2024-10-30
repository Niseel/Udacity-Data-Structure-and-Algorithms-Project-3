## Requirements
Rearrange array elements to form two numbers such that their sum is maximized. The digits are assumed to be in the range [0, 9]. The number of digits in both numbers cannot differ by more than 1. You cannot use any built-in sorting functions, and the expected time complexity is `O(n log(n))`.

**Example:** 
For the input `[1, 2, 3, 4, 5]`, the expected output could be `(531, 42)` or `(542, 31)`. Both pairs yield the maximum sum.

## Approach

### Provided Approach
The provided algorithm constructs two numbers by first counting the frequency of each digit from 0 to 9. It then builds the two numbers by alternating digits from the highest to the lowest, ensuring that the larger digits are prioritized.

- **Steps:**
  1. Count the frequency of each digit.
  2. Build two numbers by alternating the largest available digits.
  3. Convert the lists of digits to integers.

- **Time Complexity:**
  - Counting the frequency: `O(n)`
  - Constructing the numbers: `O(n)` 
  - Total: `O(n + n) => O(n)`

- **Space Complexity:**
  - Input space: `O(n)` (for the list of digits)
  - Auxiliary space: `O(1)` (a fixed-size frequency array)
  - Total: `O(n + 1) => O(n)`

### Optimal Approach (Detailed Explanation)
A more intuitive method involves the following steps:

1. **Sort the Digits:**
   Sort the digits in descending order to ensure that larger digits are placed first. This guarantees that the two numbers formed will have a higher sum.

2. **Distribute Digits:**
   Create two numbers by picking digits alternately from the sorted list. The first number takes digits at even indices, while the second number takes digits at odd indices.

3. **Convert to Integers:**
   Convert the resulting lists of digits back to integers.

- **Time Complexity:**
  - Sorting the digits: `O(n log(n))` (using a sorting algorithm such as merge sort)
  - Constructing the two numbers: `O(n)`
  - Total: `O(n log(n) + n) => O(n log(n))`

- **Space Complexity:**
  - Input space: `O(n)` (for the list of digits)
  - Auxiliary space: `O(1)` (if sorting in place)
  - Total: `O(n + 1) => O(n)`