import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    ("  hello world", "hello world"),
    (" python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "u", False),
    ("", "a", False),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("ababa", "a", "bb"),
    ("Test", "xyz", "Test"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123qwe", "123qwe"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_trim_negative():
    assert string_utils.trim("Skypro   ") == "Skypro   "


def test_delete_symbol_negative():
    assert string_utils.delete_symbol("", "a") == ""


def test_contains_negative():
    assert string_utils.contains("SkyPro", "") == False
