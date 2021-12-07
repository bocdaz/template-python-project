import os
import shutil


REMOVE_PATHS = [
    {% if cookiecutter.project_type != "FastAPI application" %}
    "src/{{cookiecutter.underscored}}/routers",
    "src/{{cookiecutter.underscored}}/config.py",
    "src/{{cookiecutter.underscored}}/dependencies.py",
    "tests/conftest.py",
    "tests/test_health.py",
    "tests/test_items.py",
    "tests/test_users.py",
    "tests/utils.py",
    {% endif %}
]


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
