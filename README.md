# litestar-chat

## For dev

### Init

Install <https://pdm-project.org/dev/> and <https://pre-commit.com>, then

    git clone git@github.com:afonasev/litestar-chat.git
    cd litestar-chat
    pre-commit install
    pdm sync

### Get all actions

    pdm run --list

### Test

    pdm run test

### Lint

    pdm run lint

### Run server

<https://github.com/emmett-framework/granian>

    pdm run server
