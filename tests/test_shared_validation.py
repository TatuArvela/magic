import contextlib
from io import StringIO

from magic.shared.spellbook import DEFAULT_SPELL
from magic.shared.validation import (
    __is_each_word_available,
    __print_validation_errors,
    has_duplicates,
    is_a_number,
    is_empty,
    is_yes_or_no,
)
from tests.utils import expect, strip_output


def test_is_a_number():
    expect(is_a_number("1")).to_be_true()
    expect(is_a_number("100")).to_be_true()
    expect(is_a_number("cat")).to_be_false()
    expect(is_a_number(" ")).to_be_false()


def test_is_yes_or_no():
    expect(is_yes_or_no("y")).to_be_true()
    expect(is_yes_or_no("yes")).to_be_true()
    expect(is_yes_or_no("n")).to_be_true()
    expect(is_yes_or_no("no")).to_be_true()
    expect(is_yes_or_no("yas")).to_be_false()
    expect(is_yes_or_no("")).to_be_false()


def test_is_empty():
    expect(is_empty([])).to_be_true()
    expect(is_empty([""])).to_be_true()
    expect(is_empty(["a"])).to_be_false()


def test_has_duplicates():
    expect(has_duplicates(["cat", "cat"])).to_be_true()
    expect(has_duplicates(["cat", "dog"])).to_be_false()


def test___is_each_word_available(snapshot):
    test_spells = {"e": DEFAULT_SPELL, "example": DEFAULT_SPELL}
    errors1 = __is_each_word_available(["a", "b", "c", "d"], test_spells)
    errors2 = __is_each_word_available(["a", "b", "c", "e"], test_spells)
    errors3 = __is_each_word_available(["add", "b", "c", "d"], test_spells)

    expect(errors1).to_be_false()
    expect(errors2).to_be_true()
    expect(errors3).to_be_true()
    snapshot.assert_match(errors2)
    snapshot.assert_match(errors3)


def test___print_validation_errors(snapshot):
    errors = [
        "Error: 'add' is a reserved word",
        "Error: 'example' is already used in a spell",
    ]

    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        __print_validation_errors(errors)
    output = strip_output(temp_stdout)
    snapshot.assert_match(output)
