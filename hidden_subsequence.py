# Implement is_subsequence, an ordered subsequence checker.

# Create hidden_subsequence.py.
# Expose def is_subsequence(needle: str, haystack: str) -> bool:.

# Return True when every character of needle can be found in haystack
# in the same order.
# Characters do not need to be adjacent.
# The comparison is case-sensitive.
# An empty needle is always a valid subsequence.

# Example :
# is_subsequence("bot", "build output tree")
# True

# is_subsequence("bto", "build output tree")
# False

# def is_subsequence(needle: str, haystack: str) -> bool:
#     i = 0

#     for char in haystack:
#         if i < len(needle) and char == needle[i]:
#             i += 1

#     return i == len(needle)

def is_subsequence(needle: str, haystack: str) -> None:
    it = iter(haystack)
    return all(c in it for c in needle)


if __name__ == "__main__":
    print(is_subsequence("bot", "build output tree"))
    print(is_subsequence("bto", "build output tree"))
