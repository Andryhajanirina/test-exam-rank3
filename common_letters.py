# Implement common_letters, a function that keeps shared characters without
# duplicates.

# Create common_letters.py.
# Expose def common_letters(left: str, right: str) -> str:.

# Scan left from start to end.
# Keep a character only if it also appears in right.
# Do not repeat a character that was already kept.

# The result order must follow the first appearance order in left.

# The comparison is case-sensitive.
# Example
# common_letters("vector", "covered")
# "vecor"

# common_letters("mno", "XYZ")
# ""

def common_letters(left: str, right: str) -> str:
    result: list[str] = []
    for c in left:
        if c in right:
            if c not in result:
                result.append(c)
    return "".join(result)


if __name__ == "__main__":
    print(common_letters("vectore", "covered"))
    print(common_letters("mno", "XYZ"))
