## Requirement
Given a sorted array that has been rotated at some random pivot point, we want to search for a target value. If found, we return its index; otherwise, we return -1.

**Example:** 
Input: `nums = [4,5,6,7,0,1,2], target = 0`  
Output: `4`

## Approach

### Provided Approach
The provided algorithm uses a binary search-like technique to locate the target value in a rotated sorted array. It checks which half of the array is sorted and determines whether the target lies in the sorted half or the unsorted half.

- **Time Complexity:** 
  - In the worst case, this approach performs binary search twice, resulting in `O(log n + log n) => O(log n)`.
  
- **Space Complexity:**
  - Input space: `O(n)` (for the array)
  - Auxiliary space: `O(n)` (for any temporary structures if needed)
  - Total: `O(n + n) => O(n)`

### Optimal Approach
A more optimal approach involves first finding the pivot point where the array is rotated. Once the pivot is identified, the array can be split into two sorted subarrays. Then, we can perform a binary search on the relevant subarray that might contain the target value.

1. **Find the Pivot:**
   Use binary search to identify the pivot point where the array changes from increasing to decreasing.

2. **Determine Which Subarray to Search:**
   Depending on the target value, decide whether to search in the left sorted part or the right sorted part.

3. **Perform Binary Search:**
   Conduct a binary search on the determined subarray to find the target.

- **Time Complexity:** 
  - Finding the pivot: `O(log n)` 
  - Binary search on one of the halves: `O(log n)`
  - Total: `O(log n + log n) => O(log n)`

- **Space Complexity:**
  - Input space: `O(n)` (for the array)
  - Auxiliary space: `O(1)` (no additional space required)
  - Total: `O(n)`