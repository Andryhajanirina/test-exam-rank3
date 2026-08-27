# Implement delimiters_balanced, a function that validates nested delimiters
# in a string.
# Create delimiter_stack.py.

# Expose def delimiters_balanced(text: str) -> bool:.
# Treat (), [], and {} as delimiter pairs.
# Characters that are not delimiters must be ignored.
# Return True only when every closing delimiter matches the latest unmatched
# opener.
# Return True for a string that contains no delimiters.

# 01
# Flat pairs
# 02
# Nested delimiters with ignored text
# 03
# Wrong closer
# 04
# Crossed pairs
# 05
# No delimiters
# 06
# Digits are ignored
# 07
# Digits inside delimiter pairs are ignored
# 08
# Unclosed opener
# 09
# Closer before opener

# examples
# delimiters_balanced("build[{ok}]")
# True

# delimiters_balanced("[(])")
# False

def delimiters_balanced(text: str) -> bool:
    stack: list[str] = []
    pairs: dict[str, str] = {
        "[": "]",
        "{": "}",
        "(": ")"
    }
    for bracket in text:
        if bracket in pairs:
            stack.append(bracket)
        elif bracket in pairs.values():
            if not stack or pairs[stack.pop()] != bracket:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(delimiters_balanced("build[{ok}]"))
    print(delimiters_balanced("[(])"))
