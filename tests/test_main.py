"""Test cases for the init module."""
from template_python_project.main import hi


def test_print_output(capfd):
    """Verify the print output of hi()."""
    hi()
    out, err = capfd.readouterr()
    assert out == "Hi from main.py!\n"
