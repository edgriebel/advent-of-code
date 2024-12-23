# https://adventofcode.com/2024/day/22
from typing import Any, Callable, List

from aoc_utils import get_data

data_simple = {
    "start": 123,
    "next": [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ],
}


def mix(secret: int, n: int) -> int:
    """
    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number.
    Then, the secret number becomes the result of that operation.
    (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    """
    return secret ^ n


def prune(secret: int) -> int:
    """
    To prune the secret number, calculate the value of the secret number modulo 16777216.
    Then, the secret number becomes the result of that operation.
    (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    """
    return secret % 16777216


def nextval(secret: int) -> int:
    """Create next secret number
    In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:
    Calculate the result of multiplying the secret number by 64.
        Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
        Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048.
        Then, mix this result into the secret number. Finally, prune the secret number.
    """

    v = secret * 64
    v1 = prune(mix(secret, v))
    # print(f"{secret=} => {v1=}")
    v2 = prune(mix(v1, v1 // 32))
    # print(f"{v1=} => {v2=}")
    v3 = prune(mix(v2, v2 * 2048))
    # print(f"{v2=} => {v3=}")
    return v3


# test mix and prune
assert (g := 37) == (v := mix(42, 15)), f"retval should be {g}, was {v}"
assert (g := 16113920) == (v := prune(100000000)), f"retval should be {g}, was {v}"

assert (g := data_simple["next"][0]) == (
    v := nextval(data_simple["start"])
), f"retval should be {g}, was {v}"

secret = data_simple["start"]
for i, given in enumerate(data_simple["next"]):
    new_sec = nextval(secret)
    # print(f"{i=}: {secret=} {given=} {new_sec=}")
    assert new_sec == given, f"{i=}: {secret=} {given=} != {new_sec=}"
    secret = new_sec

# complex test
data = {
    "start": [1, 10, 100, 2024],
    "given": [8685429, 4700978, 15273692, 8667524],
}


def do_rounds(secret: int, rounds: int) -> int:
    new_sec = secret
    for i in range(rounds):
        if i > 0 and not i % 100:
            # print(".", end="", flush=True)
            pass
        # elif i > 0 and not i % 10:
        # print(".", end="", flush=True)
        new_sec = nextval(new_sec)
    # print()
    return new_sec


values = [0] * len(data["given"])
for i in range(len(data["given"])):
    values[i] = do_rounds(data["start"][i], 2000)
    assert (g := data["given"][i]) == values[i], f"{g=} != {values[i]=}"

assert (g := 37327623) == (v := sum(values)), f"{g=} != sums: {v=}"
v = do_rounds(1, 2000)
assert (g := 8685429) == v, f"{g=} != {v=}"
print("TESTS PASS!!")

data = get_data(22, lambda x: int(x))

values = [0] * len(data)
for i, secret in enumerate(data):
    if i > 0 and not i % 250:
        print(f"{i:4} of {len(data)}")
    values[i] = do_rounds(secret, 2000)

print(f"sum: {sum(values)}")

# Part 2: ....
