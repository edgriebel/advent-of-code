# https://adventofcode.com/2024/day/4
# word search
import re
from aoc_utils import get_data
from typing import Tuple

test_data = get_data("04-test")
test_data_answer = (18, 9)
full_data = get_data("04")
data = test_data

# print(test_data)

W = "XMAS"


def find_matches(
    grid, i: int, j: int, letter=0, dir=(0, 0), vals=[], dir_hv=True
) -> int:
    if dir == (0, 0):
        if grid[i][j] != W[letter]:
            return 0
        m = 0
        if dir_hv:
            m += find_matches(grid, i, j, letter + 1, (1, 0), [(i, j)])
            m += find_matches(grid, i, j, letter + 1, (0, 1), [(i, j)])
            m += find_matches(grid, i, j, letter + 1, (-1, 0), [(i, j)])
            m += find_matches(grid, i, j, letter + 1, (0, -1), [(i, j)])
        # diagonals
        m += find_matches(grid, i, j, letter + 1, (1, 1), [(i, j)])
        m += find_matches(grid, i, j, letter + 1, (1, -1), [(i, j)])
        m += find_matches(grid, i, j, letter + 1, (-1, 1), [(i, j)])
        m += find_matches(grid, i, j, letter + 1, (-1, -1), [(i, j)])
    else:
        x, y = dir
        if i + x < 0 or i + x >= len(grid[0]) or j + y < 0 or j + y >= len(grid):
            return 0
        if grid[i + x][j + y] != W[letter]:
            return 0
        else:
            vals.append((i + x, j + y))
            # We've found the letter, let's see if we're at the end
            if letter == len(W) - 1:
                # print(f"Coords: {"".join([str(v) for v in vals])}")
                return 1
            return find_matches(grid, i + x, j + y, letter + 1, dir, vals)
    return m


def process_grid(grid, debug=False, match_method=find_matches):
    matches = 0
    for i in range(len(grid[0])):
        if len(grid) < 20:
            print(" ".join(grid[i]))
        for j in range(len(grid)):
            matches += match_method(grid, i, j)
        if debug:
            print(f"{i=} {matches=}")
    return matches


assert (a := process_grid(test_data, False)) == (
    given := test_data_answer[0]
), f"{a=} != {given=}"
assert (a := process_grid(full_data)) == (given := 2654), f"{a=} != {given=}"
print(f"Part 1 Answer: {process_grid(full_data)}")

##########
# PART 2 #
##########
# print("PART 2", process_grid(test_data, part2=True), sep="\n")


def check_x(grid, i, j, debug=False) -> int:
    if i + 3 > len(grid[0]) or j + 3 > len(grid):
        # print(f"end of array: {i=} {j=} {len(grid[0])=} {len(grid)=}")
        return 0

    v00 = grid[i][j]
    v02 = grid[i + 2][j]
    v20 = grid[i + 2][j]
    v22 = grid[i + 2][j + 2]
    v11 = grid[i + 1][j + 1]

    if i >= 2:
        debug = False
    if debug:
        print(f"{v00} {v02}\n {v11}\n{v20} {v22}")

    if v11 != "A":
        if debug:
            print("NO A")
        return 0
    v00 = grid[i][j]
    v02 = grid[i][j + 2]
    v20 = grid[i + 2][j]
    v22 = grid[i + 2][j + 2]
    # ends can only have M or S, not X or A
    if "A" in v00 + v02 + v20 + v22 or "X" in v00 + v02 + v20 + v22:
        if debug:
            print("has M or X")
        return 0
    if v00 != v22 and v02 != v20:
        return 1
    if debug:
        print(f"{v00} == {v22} or {v02} == {v20}")
    return 0


print("check_x", process_grid(test_data, debug=False, match_method=check_x))
assert (a := process_grid(test_data, debug=False, match_method=check_x)) == (
    given := test_data_answer[1]
), f"{a=} != {given:=}"

assert (a := process_grid(full_data, debug=False, match_method=check_x)) == (
    given := 1990
), f"{a=} != {given:=}"
