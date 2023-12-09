# https://www.structlog.org/en/stable/standard-library.html#rendering-using-logging-based-formatters
import logging
import sys

import structlog

# PEP 695 (type alias) not yet supported in mypy
LogLevel = int
LogRenderer = structlog.dev.ConsoleRenderer | structlog.processors.JSONRenderer


def configure_logging(level: LogLevel = logging.INFO) -> None:
    _configure_loggers()
    set_log_level(level)


def set_log_level(level: LogLevel) -> None:
    logging.root.setLevel(level)


def _configure_loggers() -> None:
    # These run ONLY on entries that do originate WITHIN structlog.
    structlog_processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ]

    # These run ONLY on entries that do NOT originate within structlog.
    logging_processors = [
        structlog.stdlib.ExtraAdder(),
    ]

    # These run on ALL entries
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.CallsiteParameterAdder(
            {
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.LINENO,
            },
        ),
        _clean_event_dict,
    ]

    if sys.stderr.isatty():
        # Pretty printing when we run in a terminal session.
        # Automatically prints pretty tracebacks when "rich" is installed
        shared_processors.append(structlog.dev.ConsoleRenderer())  # pragma: no cover

    else:
        # Print JSON when we run, e.g., in a Docker container.
        # Also print structured tracebacks.
        # TODO(@afonasev): use orjson
        shared_processors.append(structlog.processors.format_exc_info)
        shared_processors.append(structlog.processors.JSONRenderer())

    # configure structlog
    structlog.configure_once(
        processors=structlog_processors,  # type: ignore[arg-type]
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # configure logging
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=logging_processors,
        processors=shared_processors,  # type: ignore[arg-type]
    )

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


def _clean_event_dict(
    _: structlog.typing.WrappedLogger,
    __: str,
    event_dict: structlog.typing.EventDict,
) -> structlog.typing.EventDict:
    event_dict.pop("_logger", None)
    event_dict.pop("_name", None)
    event_dict.pop("_record", None)
    event_dict.pop("_from_structlog", None)
    return event_dict
