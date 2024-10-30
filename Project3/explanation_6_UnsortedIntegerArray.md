**Requirement:**
Implement a function that finds the smallest and largest integers from a list of unsorted integers. The implementation should run in \(O(n)\) time complexity without using Python's built-in functions for finding minimum and maximum values.

**Approach:**

Initially assume that `min` and `max` values are the first element of the array. Use linear search algorithm to check if the current element is greater/lesser than min/max values. Update them accordingly and return (min, max) values in a tuple format.

**Complexity Analysis:**

*Time complexity*  
- `O(n)` // n is length of array

*Space complexity:*

- Input space => `O(n)`
- Auxiliary space => `O(1)`
- Total space => `O(n + 1)`  => `O(n)`