# 01
# Rectangular grid
# 02
# Empty row
# 03
# Empty grid
# 04
# Negative values
# 05
# Single row
# 06
# Input grid is not mutated
# mirror_rows([[8, 1, 4], [3, 5, 9]])
# [[4, 1, 8], [9, 5, 3]]

# mirror_rows([[6], [], [7, 8]])
# [[6], [], [8, 7]]

def mirror_rows(grid: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in grid]


if __name__ == "__main__":
    print(mirror_rows([[6], [], [7, 8]]))
