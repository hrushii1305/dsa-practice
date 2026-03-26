class twopointers:
    def pair_sum(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return None  # Return None if no pair is found


obj=twopointers()
print(obj.pair_sum([1, 2, 3, 4, 5], 9))  # Output: [3, 4]