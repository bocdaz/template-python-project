"""Test cases for `{{ cookiecutter.project_slug }}` package."""
import {{cookiecutter.project_slug}}


def test_version():
    """Verify the {{ cookiecutter.project_slug }} package version."""
    assert {{cookiecutter.project_slug}}.__version__ == "{{ cookiecutter.version }}"


def test_print_output(capfd):
    """Verify the print output of hi()."""
    {{cookiecutter.project_slug}}.main.hi()
    out, err = capfd.readouterr()
    assert out == "Hi from main.py!\n"
