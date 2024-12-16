# https://adventofcode.com/2024/day/11

from typing import List

data1 = [0, 1, 10, 99, 999]
data2 = [125, 17]
data3 = [7568, 155731, 0, 972, 1, 6919238, 80646, 22]


def doit(x) -> List[int]:
    if x == 0:
        return [1]

    v = list(str(x))
    if len(v) % 2 == 0:
        # v1, v2 = v[: len(v) // 2], v[len(v) // 2 :]
        return [
            int(
                "".join(
                    v[: len(v) // 2],
                )
            ),
            int("".join(v[len(v) // 2 :])),
        ]

    return [x * 2024]


def around(data):
    newvals = []
    for d in data:
        newvals.extend(doit(d))
    return newvals


assert around(data1) == [1, 2024, 1, 0, 9, 9, 2021976]
assert around(data2) == [253000, 1, 7]
print(around(data1))

data = data3
times = 55
for t in range(times):
    newvals = around(data)
    # print(f"blink {t}: {newvals}")
    print(f"{t:2} l={len(newvals):,}", end=" ", flush=True)
    data = newvals

print(f"Count: {len(data)}")
