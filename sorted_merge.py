# Implement merge_sorted_values, a function
# that merges two sorted integer lists.

# Create sorted_merge.py.
# Expose def merge_sorted_values(left: list[int], right: list[int])
# -> list[int]:.

# Both input lists are already sorted in ascending order.
# Return a new list containing every value from both inputs in ascending order.
# Preserve duplicate values.
# Handle empty lists.
# Do not mutate either input list.

# Example:
# merge_sorted_values([-3, 4, 9], [-2, 4, 10])
# [-3, -2, 4, 4, 9, 10]

# merge_sorted_values([], [5, 8])
# [5, 8]

def merge_sorted_values(left: list[int], right: list[int]) -> list[int]:
    return sorted(left + right)


if __name__ == "__main__":
    print(merge_sorted_values([-3, 4, 9], [-2, 4, 10]))
    print(merge_sorted_values([], [5, 8]))
