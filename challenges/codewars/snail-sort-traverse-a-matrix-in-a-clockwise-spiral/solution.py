# Snail Sort — Traverse a Matrix in a Clockwise Spiral
# Codewars 4 kyu: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#
# Approach: peel + rotate trick
# After collecting the top row (left→right), rotate the remaining matrix
# 90° counter-clockwise so the next ring's top row is ready to peel.
# One pop(0) + one rotation = one side of the spiral. Repeat until empty.


def snail(snail_map):
    """Return all matrix elements in clockwise spiral order."""
    result = []
    while snail_map:
        # Peel the top row (left → right)
        result += list(snail_map.pop(0))
        # Rotate remaining 90° counter-clockwise:
        # zip(*m) transposes, [::-1] reverses row order → CCW rotation
        # This makes the right column the new top row (down → right)
        if snail_map and snail_map[0]:
            snail_map = [list(row) for row in zip(*snail_map)][::-1]
    return result


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    assert snail([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert snail([[1,  2,  3,  4],
                  [5,  6,  7,  8],
                  [9,  10, 11, 12],
                  [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    assert snail([[1]]) == [1]
    assert snail([[]]) == []
    assert snail([]) == []

    print("All tests passed ✓")
