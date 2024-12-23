# https://adventofcode.com/2024/day/3
import re
from typing import List
from aoc_utils import get_data

data = "mul(123,456)"
data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
ans = 161

in_do: bool = True  # Yuck, global...


def getvals(vals: List[str], do: bool = True, no_skip: bool = True) -> int:
    global in_do
    in_do = do
    tot = 0
    eq_pat = re.compile(r"mul.(\d+),(\d+)\)")
    for eq in vals:
        print(f"{eq=}")
        if "don't" in eq:
            print("Dont")
            in_do = False
        elif "do" in eq:
            print("DO")
            in_do = True
        elif in_do or no_skip:
            match = eq_pat.search(eq)
            print("m1", match.group(1), end="\t")
            print("m2", match.group(2))
            tot += int(match.group(1)) * int(match.group(2))
        else:
            print(f"SKIP: {eq=}")
    print()
    return tot


mul_pat = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

vals = mul_pat.findall(data)
# print(vals)
assert ans == (_v := getvals(vals)), f"{ans} != {_v}"

data = get_data("03")

total = 0
for l in data:
    total += getvals(mul_pat.findall(l))

print(total)
assert total == (_ans := 160672468), f"Part 1 broken: {total=} != {_ans}"

assert 160672468 == getvals(mul_pat.findall(" ".join(data)))
## PART 2
test_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
test_ans = 48

test_tot = getvals(mul_pat.findall(test_data), True, False)
assert test_tot == test_ans, f"{test_tot=} != {test_ans=}"

pt2_tot = getvals(mul_pat.findall(" ".join(data)), True, False)
print(pt2_tot)

assert pt2_tot == 84893551
