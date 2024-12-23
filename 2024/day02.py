# https://adventofcode.com/2024/day/2
from aoc_utils import get_data

ex_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().split(
    "\n"
)
ex_res = [True, False, False, False, False, True]

ex_data = [l.split(" ") for l in ex_data]
# print(ex_data)


def safe(rec):
    up = False
    val = int(rec[0])
    if int(rec[1]) > val:
        up = True
    print(f"{rec=}: {up=}")

    for v in rec[1:]:
        v = int(v)
        # print(f"{rec=}: {up=} {val=} {v=}")
        if (up and val < v and v - val <= 3) or (not up and val > v and val - v <= 3):
            val = v
        else:
            return False

    return True


retvals = [safe(rec) for rec in ex_data]
assert retvals == ex_res

print(f"Safe: {sum([1 if safe(rec) else 0 for rec in ex_data])}")

data = get_data("02", lambda x: x.split(" "))

print(data[:5], len(data))


ans = sum([1 if safe(rec) else 0 for rec in data])
print(f"Safe: {ans}")
assert 220 == ans

##########
# Part 2 #
##########
