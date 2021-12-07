# {{cookiecutter.project_name}}

## Dev Setup

### Prerequisites
- [Poetry](https://python-poetry.org/), install it with `pip install --user poetry`.

### Installation
1. Run `poetry install`
2. Install precommit

    ```bash
    pip install --user --upgrade nox pre-commit
    ```

3. Run `pre-commit install`

### Getting Started
1. Run `poetry shell`
2. Modify the project name and authors in [pyproject.toml](./pyproject.toml)
3. Start adding new python files to [src](./src) and new tests to [tests](./tests)
4. (Optional) If using DevSpace:
    * Run `devspace use context` to select the proper cluster.
	* Run `devspace use namespace my-namespace` to select the namespace to use.
	* Start your project in development mode with `devspace dev`.

### Running Dev Tools
1. Change to the base directory
2. In cmd/terminal use `nox` to run **ALL** linter, security checks, and tests
  - Use `nox --list-sessions` to list all possible sessions
  - Use `nox -rs lint` to run the linter
  - Use `nox -rs safety` to run security checks
  - Use `nox -rs tests` to run test suites
  - Use `nox -rs black` to run the formatter


## FAQ

#### How do I run my python file with poetry?

```bash
poetry shell
poetry run ___.py
```

#### How do I install new libraries to my project?

`poetry add ___`

## Useful Resources

- [Python Coding Conventions](https://itswiki.bank-banque-canada.ca/display/AECUR/Python+coding+conventions)
- [Unit Tests](https://docs.pytest.org/en/latest/)
- [Docstrings](https://www.python.org/dev/peps/pep-0257/)
- [Auto-docs](https://www.mkdocs.org/#overview)
- [Formatter](https://github.com/psf/black)
- [Typing](https://docs.python.org/3/library/typing.html)
- [How to branch and merge in git](https://itswiki.bank-banque-canada.ca/display/AECUR/Introduction+to+GitHub#IntroductiontoGitHub-Branchingandmerging)
- [How to make a pull request (PR)](https://itswiki.bank-banque-canada.ca/display/AECUR/Introduction+to+GitHub#IntroductiontoGitHub-CreatingaPullRequest(PR))
- [The Code Review Developer Guide](https://itswiki.bank-banque-canada.ca/display/AECUR/Code+Review+Developer+Guide)


## Included tools

|Name|Purpose|
|----|----|
|[coverage.py](https://coverage.readthedocs.io)|Coverage.py is a tool for measuring code coverage of Python programs.|
|[flake8](https://github.com/pycqa/flake8)|Flake8 is a wrapper around various linting tools, and provides a plggable interface.|
|[flake8-bandit](https://pypi.org/project/flake8-bandit/)|[Bandit](https://bandit.readthedocs.io/en/latest/) is a tool designed to find common security issues in Python code.|
|[flake8-black](https://github.com/peterjc/flake8-black)|This is an MIT licensed [flake8](https://github.com/pycqa/flake8) plugin for validating Python code style with the command line code formatting tool [black](https://github.com/psf/black).|
|[flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)|A plugin for Flake8 finding likely bugs and design problems in your program.|
|[flake8-docstrings](https://github.com/PyCQA/flake8-docstrings)|A simple module that adds an extension for the fantastic [pydocstyle](https://github.com/pycqa/pydocstyle) tool to [flake8](https://github.com/pycqa/flake8).|
|[isort](https://pycqa.github.io/isort/)|isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.|
|[nox](https://nox.thea.codes/en/stable/)|`nox` is a command-line tool that automates testing in multiple Python environments, similar to [tox](https://tox.readthedocs.org/).|
|[poetry](https://python-poetry.org/)|Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere.|
|[pre-commit](https://pre-commit.com/)|A framework for managing and maintaining multi-language pre-commit hooks.|
|[pytest](https://docs.pytest.org/)|The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.|
|[pytest-cov](https://github.com/pytest-dev/pytest-cov)|This pytest plugin produces test coverage reports.|
|[pytest-mock](https://github.com/pytest-dev/pytest-mock/)|This pytest plugin provides a `mocker` fixture which is a thin-wrapper around the patching API provided by the [mock](https://docs.python.org/dev/library/unittest.mock.html) package.|
|[safety](https://pyup.io/safety/)|Safety checks your dependencies for known security vulnerabilities.|
|[xdoctest](https://github.com/Erotemic/xdoctest)|The `xdoctest` package is a re-write of Python's builtin `doctest` module.|
