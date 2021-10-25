FROM python:3.9.7-slim-buster as development

# Create project directory (workdir)
WORKDIR /app

# Add pyproject.toml to WORKDIR and install dependencies
COPY pyproject.toml .
RUN pip install poetry && poetry install

# Add source code files to WORKDIR
ADD . .

# Application port (optional)
EXPOSE 8080

# Container start command
# It is also possible to override this in devspace.yaml via images.*.cmd
CMD ["poetry", "run", "python", "src/template_python_project/main.py"]
