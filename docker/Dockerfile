# build stage
FROM python:3.12 AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /app/
COPY app/ /app/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.12

# retrieve packages from build stage
ENV PYTHONPATH=/app/pkgs
COPY --from=builder /app/__pypackages__/3.12/lib /app/pkgs

# retrieve executables
COPY --from=builder /app/__pypackages__/3.12/bin/* /bin/

# set command/entrypoint, adapt to fit your needs
CMD ["python", "-m", "app"]
