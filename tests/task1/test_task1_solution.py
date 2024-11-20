import pytest
from task1.solution import strict


@strict
def add(a: int, b: int) -> int:
    return a + b


def test_add_correct_types():
    assert add(2, 3) == 5


def test_add_incorrect_types():
    with pytest.raises(TypeError, match="Argument 'b' must be of type int"):
        add(2, "3")


@strict
def concat(a: str, b: str) -> str:
    return a + b


def test_concat_correct_types():
    assert concat("hello", "world") == "helloworld"


def test_concat_incorrect_types():
    with pytest.raises(TypeError, match="Argument 'a' must be of type str"):
        concat(42, "world")
