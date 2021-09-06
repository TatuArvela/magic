import contextlib
from io import StringIO

from magic.shared.display import Color, clear_last_line, in_color, print_error
from tests.utils import strip_output


def test_in_color(snapshot):
    color_samples = []
    for color in Color:
        color_samples.append(in_color("test", color))
    snapshot.assert_match(color_samples)


def test_print_error(snapshot):
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        print_error("test")
    output = strip_output(temp_stdout)
    snapshot.assert_match(output)


def test_clear_last_line(snapshot):
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        clear_last_line()
    output = strip_output(temp_stdout)
    snapshot.assert_match(output)
