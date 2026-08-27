# Implement zigzag_letters, a text formatter that alternates letter casing.
# Create zigzag_case.py.
# Expose def zigzag_letters(text: str) -> str:.

# Return a new string where alphabetic characters alternate between lowercase
# and uppercase.
# The first alphabetic character must be lowercase, the second uppercase,
# the third lowercase, and so on.
# Non-alphabetic characters must stay unchanged.
# Non-alphabetic characters do not advance the alternating letter counter.
# The alternation does not reset after spaces or punctuation.

# examples
# zigzag_letters("grade")
# "gRaDe"

# zigzag_letters("ab-cd ef")
# "aB-cD eF"

# def string_sculptor(text: str) -> str:
#     """
#     Transforms a string by alternating the case
#     of alphabetic characters only.
#     Non-alphabetic characters remain unchanged and are
#     NOT counted in the alternation index.
#     The first alphabetic character should be lowercase,
#     the second uppercase, etc. Spaces reset the alternation
#     (next alpha after a space is lowercase again).
#     """
#     to_low: bool = True
#     res: str = ""
#     for i in range(len(text)):
#         if text[i].isspace():
#             to_low = True
#         if text[i].isalpha():
#             if to_low:
#                 res += text[i].lower()
#                 to_low = False
#             else:
#                 res += text[i].upper()
#                 to_low = True
#         else:
#             res += text[i]
#     return res

def zigzag_letters(text: str) -> str:
    result: str = ""
    to_low: bool = True
    for i in range(len(text)):
        if text[i].isalpha():
            if to_low:
                result += text[i].lower()
                to_low = False
            else:
                result += text[i].upper()
                to_low = True
        else:
            result += text[i]
    return result


if __name__ == "__main__":
    print(zigzag_letters("grade"))
    print(zigzag_letters("ab-cd ef"))
