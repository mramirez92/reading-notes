import pytest
# from package_name.module_name import  funct_name

from fizz_buzz.fizz_buzz import fizz_buzz

# pytest tests must start with "test_"

# end goal in mind= test drives development

# each function in test gets invoked by py test


def test_function_exists():
    # pass
    assert fizz_buzz


@pytest.mark.skip()
def test_fizz_buzz_3():
    actual = fizz_buzz(3)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_6():
    actual = fizz_buzz(6)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_5():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_fizz_buzz_15():
    actual = fizz_buzz(15)
    expected = "FizzBuzz"
    assert actual == expected


def test_fizz_buzz_7():
    actual = fizz_buzz(7)
    expected = "7"
    assert actual == expected


def test_fizz_buzz_8():
    actual = fizz_buzz(8)
    expected = "8"
    assert actual == expected
