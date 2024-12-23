# https://adventofcode.com/2024/day/1
import re
from aoc_utils import get_data

data = get_data("01")
# with open('day1_input.txt') as f:
# data = f.readlines()
test_data = """
3   4
4   3
2   5
1   3
3   9
3   3
""".split("\n")[1:-1]
# print(test_data)
# data = test_data
data = [re.split(" +", l.strip()) for l in data]

a, b = [], []
for x, y in data:
    a += [int(x)]
    b += [int(y)]

a = sorted(a)
b = sorted(b)

# print(len(a), len(b), a[:5], b[:5])

sums = 0
for i in range(len(a)):
    sums += abs(a[i] - b[i])

print(f"Part 1: {sums}")
assert 1530215 == sums

########
# Part 2
########

# figure similarity score

# put list 2 into a dict with value is count
from collections import defaultdict

counts = defaultdict(lambda: 0)
for v in b:
    counts[v] += 1
simscore = 0
for v in a:
    simscore += v * counts[v]

print(f"Part 2: {simscore}")
assert 26800609 == simscore
