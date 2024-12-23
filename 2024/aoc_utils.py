from typing import Any, Callable, List, Union


def get_data(
    day: Union[str, int], func: Callable[[str], Any] = lambda x: x
) -> List[Any]:
    with open(f"day{day}.data") as f:
        data = [func(l.strip()) for l in f.readlines()]
    return data
