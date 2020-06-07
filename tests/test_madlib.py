import pytest

from madlib_cli.madlib import (
    welcome_screen,
    read_template,
)

def test_welcome_screen_exists():
    assert welcome_screen


# @pytest.mark.skip
def test_read_template_exists():
    assert read_template


# You are NOT required to test terminal input/output, AKA print and input functions.
# Break down your code so that it is more easily testable.


# Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.


def test_read_template_returns():
    expected = "Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.\n"
    actual = read_template()
    assert actual == expected


# Create and test a parse function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
# Stretch Goals
# Figure out / research a way to verify terminal input/output.
# Test that completed madlib is properly written to disk with correct content.
