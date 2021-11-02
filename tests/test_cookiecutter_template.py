from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_fastapi_application(tmpdir):
    generate(
        tmpdir,
        {
            "full_name": "Philip Fry",
            "email": "zzzz@bank-bakque-canada.ca",
            "project_name": "Test Python Project",
            "hyphenated": "test-python-project",
            "underscored": "test_python_project",
            "project_short_description": "A project to test out cookiecutter.",
            "project_type": "FastAPI application",
            "version": "0.1.0",
        },
    )
    assert paths(tmpdir) == {
        "test-python-project",
        "test-python-project/.dockerignore",
        "test-python-project/.flake8",
        "test-python-project/.gitignore",
        "test-python-project/.pre-commit-config.yaml",
        "test-python-project/CHANGELOG.md",
        "test-python-project/Dockerfile",
        "test-python-project/README.md",
        "test-python-project/devspace.yaml",
        "test-python-project/devspace_start.sh",
        "test-python-project/docs",
        "test-python-project/docs/changelog.md",
        "test-python-project/docs/index.md",
        "test-python-project/mkdocs.yml",
        "test-python-project/noxfile.py",
        "test-python-project/pyproject.toml",
        "test-python-project/src",
        "test-python-project/src/test_python_project",
        "test-python-project/src/test_python_project/__init__.py",
        "test-python-project/src/test_python_project/config.py",
        "test-python-project/src/test_python_project/dependencies.py",
        "test-python-project/src/test_python_project/main.py",
        "test-python-project/src/test_python_project/routers",
        "test-python-project/src/test_python_project/routers/__init__.py",
        "test-python-project/src/test_python_project/routers/health.py",
        "test-python-project/src/test_python_project/routers/items.py",
        "test-python-project/src/test_python_project/routers/users.py",
        "test-python-project/tests",
        "test-python-project/tests/__init__.py",
        "test-python-project/tests/conftest.py",
        "test-python-project/tests/test_health.py",
        "test-python-project/tests/test_init.py",
        "test-python-project/tests/test_items.py",
        "test-python-project/tests/test_main.py",
        "test-python-project/tests/test_users.py",
        "test-python-project/tests/utils.py",
    }


def test_python_package(tmpdir):
    generate(
        tmpdir,
        {
            "full_name": "Philip Fry",
            "email": "zzzz@bank-bakque-canada.ca",
            "project_name": "Test Python Project",
            "hyphenated": "test-python-project",
            "underscored": "test_python_project",
            "project_short_description": "A project to test out cookiecutter.",
            "project_type": "Python package",
            "version": "0.1.0",
        },
    )
    assert paths(tmpdir) == {
        "test-python-project",
        "test-python-project/.dockerignore",
        "test-python-project/.flake8",
        "test-python-project/.gitignore",
        "test-python-project/.pre-commit-config.yaml",
        "test-python-project/CHANGELOG.md",
        "test-python-project/Dockerfile",
        "test-python-project/README.md",
        "test-python-project/devspace.yaml",
        "test-python-project/devspace_start.sh",
        "test-python-project/docs",
        "test-python-project/docs/changelog.md",
        "test-python-project/docs/index.md",
        "test-python-project/mkdocs.yml",
        "test-python-project/noxfile.py",
        "test-python-project/pyproject.toml",
        "test-python-project/src",
        "test-python-project/src/test_python_project",
        "test-python-project/src/test_python_project/__init__.py",
        "test-python-project/src/test_python_project/main.py",
        "test-python-project/tests",
        "test-python-project/tests/__init__.py",
        "test-python-project/tests/test_init.py",
        "test-python-project/tests/test_main.py",
    }


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
