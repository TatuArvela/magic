from magic import app


def test_app(capsys):
    app.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
