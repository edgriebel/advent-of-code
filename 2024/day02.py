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

with open("day2.data") as f:
    data = f.readlines()
data = [l.strip().split(" ") for l in data]

print(data[:5], len(data))


print(f"Safe: {sum([1 if safe(rec) else 0 for rec in data])}")

##########
# Part 2 #
##########
