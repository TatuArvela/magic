import contextlib
from io import StringIO

from magic.shared.display import clear_last_line, print_error
from tests.utils import strip_output


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
