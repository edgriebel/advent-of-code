# https://adventofcode.com/2024/day/23
import re
from typing import Dict, List
from collections import defaultdict
from aoc_utils import get_data

# data = get_data("23", lambda x: x.split("-"))
data = get_data("23-test", lambda x: x.split("-"))

conn: Dict[str, List[str]] = defaultdict(lambda: list())

for c1, c2 in data:
    conn[c1].append(c2)
    conn[c2].append(c1)

[print(k, v) for k, v in conn.items()]
print("-" * 10)
[
    print(k, v)
    for k, v in conn.items()
    if k[0] == "t" or v[0][0] == "t" or "-t" in "-".join(v)
]
