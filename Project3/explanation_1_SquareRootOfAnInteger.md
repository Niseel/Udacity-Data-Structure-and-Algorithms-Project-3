## Requirement
To find the square root of an integer in `O(log(n))` time complexity without using any Python library.

## Summary

### Naïve Approach
- **Description:** 
  To find the floor of the square root, we start with the natural number 1 and continue to increment it by 1 until the square of that number exceeds the input number.

- **Complexity Analysis:**
  - **Time Complexity:** `O(√n)`  
    This is because we may potentially check all numbers up to √n.
  
  - **Space Complexity:**
    - **Input Space:** `O(1)` (the input number)
    - **Auxiliary Space:** `O(1)` (no extra space used)
    - **Total Space:** `O(1 + 1)` => `O(2)` => `O(1)`

### Optimized Approach
- **Description:** 
  We optimize the Naïve approach using the Binary Search algorithm. This method continuously narrows down the search space until we find the largest integer whose square is less than or equal to the input number.

- **Complexity Analysis:**
  - **Time Complexity:** `O(log(n))`  
    The time complexity is dominated by the Binary Search method, which halves the search space in each iteration.
  
  - **Space Complexity:**
    - **Input Space:** `O(1)` (the input number)
    - **Auxiliary Space:** `O(1)` (only a few variables are used)
    - **Total Space:** `O(1 + 1)` => `O(2)` => `O(1)`