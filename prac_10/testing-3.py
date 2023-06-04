"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"

    # Test if Car sets the odometer correctly
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"

    test_car = Car()  # Test with default fuel value
    assert test_car.fuel == 0, "Car does not set fuel correctly"


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('testing the function')
    'Testing the function.'
    """
    if phrase[-1] != '.':
        phrase = phrase.capitalize() + '.'
    return phrase


run_tests()
doctest.testmod()
