from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree
import pytest

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporary directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the command output
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None


commands = ["black", "docs", "lint", "safety", "tests"]


@pytest.mark.parametrize("command", commands, ids=commands)
def test_bake_and_run_nox(cookies, command):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        project_path = str(result.project_path)
        assert run_inside_dir("poetry install --no-interaction", project_path) == 0
        assert run_inside_dir(f"poetry run nox -rs {command}", project_path) == 0


def test_bake_fastapi_application(cookies):
    context = {"project_type": "FastAPI application"}
    result = cookies.bake(extra_context=context)
    pyproject_path = result.project_path / "pyproject.toml"
    with pyproject_path.open("r") as pyproject_file:
        contents = pyproject_file.read()
        assert "fastapi" in contents
        assert "tool.poetry.scripts" in contents


def test_bake_python_package(cookies):
    context = {"project_type": "Python package"}
    result = cookies.bake(extra_context=context)
    pyproject_path = result.project_path / "pyproject.toml"
    with pyproject_path.open("r") as pyproject_file:
        contents = pyproject_file.read()
        assert "fastapi" not in contents
        assert "tool.poetry.scripts" not in contents
