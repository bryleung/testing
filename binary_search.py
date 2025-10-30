def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: A sorted list of elements
        target: The element to search for
    
    Returns:
        The index of the target element if found, otherwise -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def run_tests():
    """Run test cases for binary search."""
    
    print("Binary Search Tests")
    print("-" * 40)
    
    # Test 1: Element found
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15]
    result1 = binary_search(arr1, 7)
    print(f"Test 1: {arr1}, target=7")
    print(f"Result: {result1} ✓" if result1 == 3 else f"Result: {result1} ✗")
    
    # Test 2: Element not found
    arr2 = [1, 3, 5, 7, 9]
    result2 = binary_search(arr2, 8)
    print(f"\nTest 2: {arr2}, target=8")
    print(f"Result: {result2} ✓" if result2 == -1 else f"Result: {result2} ✗")
    
    # Test 3: Empty array
    arr3 = []
    result3 = binary_search(arr3, 5)
    print(f"\nTest 3: {arr3}, target=5")
    print(f"Result: {result3} ✓" if result3 == -1 else f"Result: {result3} ✗")
    
    # Test 4: Single element
    arr4 = [5]
    result4 = binary_search(arr4, 5)
    print(f"\nTest 4: {arr4}, target=5")
    print(f"Result: {result4} ✓" if result4 == 0 else f"Result: {result4} ✗")
    
    # Test 5: First element
    arr5 = [2, 4, 6, 8, 10]
    result5 = binary_search(arr5, 2)
    print(f"\nTest 5: {arr5}, target=2")
    print(f"Result: {result5} ✓" if result5 == 0 else f"Result: {result5} ✗")
    
    # Test 6: Last element
    arr6 = [2, 4, 6, 8, 10]
    result6 = binary_search(arr6, 10)
    print(f"\nTest 6: {arr6}, target=10")
    print(f"Result: {result6} ✓" if result6 == 4 else f"Result: {result6} ✗")
    
    print("-" * 40)


if __name__ == "__main__":
    run_tests()

