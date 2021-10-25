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
