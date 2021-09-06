# Syntactic sugar


class Expect:
    def __init__(self, value):
        self.value = value

    def to_be_true(self):
        assert self.value

    def to_be_false(self):
        assert not self.value

    def to_be(self, value):
        assert value == self.value


def expect(value):
    return Expect(value)


def strip_output(output):
    return output.getvalue().strip()
