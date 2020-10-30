from .context import magic

def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    magic.Magic.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
