def rotated_array_search(input_list, number):
    """
    Find the index of a target number in a rotated sorted array using binary search.

    Args:
       input_list(array): The rotated sorted array to search in.
       number(int): The target number to find.
    Returns:
       int: The index of the target number if found, otherwise -1.
    """
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if input_list[mid] == number:
            return mid  # Target found at mid

        # Determine which half is sorted (left or right)
        if input_list[low] <= input_list[mid]:  # Left half is sorted
            if input_list[low] <= number < input_list[mid]:
                high = mid - 1  # Target is in the left half
            else:
                low = mid + 1  # Target is in the right half
        else:  # Right half is sorted
            if input_list[mid] < number <= input_list[high]:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half

    return -1  # Target not found


# Test cases
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_cases = [
    ([4, 5, 6, 7, 0, 1, 2], 6),  # Expected Output: 2
    ([4, 5, 6, 7, 0, 1, 2], 4),  # Expected Output: 0
    ([4, 5, 6, 7, 0, 1, 2], 2),  # Expected Output: 6
    ([4, 5, 6, 7, 0, 1, 2], 3),  # Expected Output: -1
    ([2, 2, 2, 3, 4, 2], 3),     # Expected Output: 3
]

# Run test cases
for test in test_cases:
    test_function(test)