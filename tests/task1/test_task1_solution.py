import pytest
from task1.solution import strict


@strict
def add(a: int, b: int) -> int:
    return a + b


@strict
def add2(a: int, b: int, *, multiplier: int = 1) -> int:
    return (a + b) * multiplier


def test_add_correct_types():
    assert add(2, 3) == 5


def test_add_incorrect_types():
    with pytest.raises(TypeError, match="Argument 'b' must be of type int"):
        add(2, "3")


def test_add2_correct_types_with_named_argument():
    assert add2(2, 3, multiplier=2) == 10


def test_add2_incorrect_named_argument_type():
    with pytest.raises(TypeError, match="Argument 'multiplier' must be of type int"):
        add2(2, 3, multiplier="2")


def test_add2_default_named_argument():
    assert add2(2, 3) == 5


@strict
def concat(a: str, b: str) -> str:
    return a + b


@strict
def concat2(a: str, b: str, *, prefix: str = "", suffix: str = "") -> str:
    return prefix + a + b + suffix


def test_concat_correct_types():
    assert concat("hello", "world") == "helloworld"


def test_concat_incorrect_types():
    with pytest.raises(TypeError, match="Argument 'a' must be of type str"):
        concat(42, "world")


def test_concat_correct_types_with_named_arguments():
    result = concat2("hello", "world", prefix="<<<", suffix=">>>")
    assert result == "<<<helloworld>>>"


def test_concat_incorrect_named_argument_type():
    with pytest.raises(TypeError, match="Argument 'prefix' must be of type str"):
        concat2("hello", "world", prefix=123, suffix=">>>")

