# def rotate_right(values: list[int], steps: int) -> list[int]:
#     return values[len(values) - steps:] + values[:len(values) - steps]

def rotate_right(values: list[int], steps: int) -> list[int]:
    if not values:
        return []
    shift = steps % len(values)
    return values[-shift:] + values[:-shift]


if __name__ == "__main__":
    print(rotate_right([9, 8, 7, 6, 5], 2))
    print(rotate_right([4, 5, 6], 4))
