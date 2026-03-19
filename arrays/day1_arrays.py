def find_max(arr):
    if not arr:
        return None  # Return None for an empty array

    max_value = arr[0]  # Initialize max_value to the first element

    for num in arr:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found

    return max_value

def array_sum(arr):
    total = 0  # Initialize total to 0

    for num in arr:
        total += num  # Add each number to the total

    return total
def count_even(arr):
    count=0
    for num in arr:
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increment count if it's even
    return count

print(find_max([3, 1, 4, 1, 5, 9]))  # Output: 9
print(array_sum([3, 1, 4, 1, 5, 9]))  # Output: 23
print(count_even([3, 1, 4, 1, 5, 9]))  # Output: 1
