# Implement count_digit_steps, a function that counts adjacent increasing
# digit pairs.

# Create digit_steps.py.
# Expose def count_digit_steps(text: str) -> int:.

# A valid pair is made of two adjacent characters that are both digits.
# The second digit must be exactly one greater than the first digit.
# Pairs may overlap, so 123 contains two valid pairs.
# 90 is not valid; there is no wraparound.
# Non-digit characters break adjacency.

# Example :
# count_digit_steps("4567")
# 3

# count_digit_steps("4q56")
# 1

def count_digit_steps(text: str) -> int:
    count: int = 0

    for i in range(len(text) - 1):
        if (
            text[i].isdigit() and
            text[i + 1].isdigit() and
            (int(text[i]) + 1 == int(text[i + 1]))
        ):
            count += 1
    return count


if __name__ == "__main__":
    print(count_digit_steps("4567"))
    print(count_digit_steps("4q56"))
