# litestar-chat

## Features

- Packaging and dependency management with [PDM](https://pdm-project.org)
- Linting with [pre-commit](https://pre-commit.com) and [ruff](https://github.com/astral-sh/ruff)
- Continuous integration with [GitHub Actions](https://github.com/features/actions)
- NOT YET Documentation with ...
- NOT YET Automated uploads to [PyPI](https://pypi.org/)
- Automated release notes with [Release Drafter](https://github.com/release-drafter/release-drafter)
- Automated dependency updates with [Dependabot](https://github.com/dependabot/dependabot-core)
- Code formatting with [ruff](https://github.com/astral-sh/ruff)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Code coverage with [Coverage.py](https://coverage.readthedocs.io/)
- Static type-checking with [mypy](http://mypy-lang.org/)
- Manage project labels with [GitHub Labeler](https://github.com/marketplace/actions/github-labeler)

The project supports **Python 3.12**.

## For developers

### Init local environment

Install <https://pdm-project.org/dev/> and <https://pre-commit.com>, then

    git clone git@github.com:afonasev/litestar-chat.git
    cd litestar-chat
    pre-commit install
    pdm sync

### Get all actions

    pdm run --list

### Run tests

    pdm run test

### Run linters

    pdm run lint

### Run server

<https://github.com/emmett-framework/granian>

    pdm run server
