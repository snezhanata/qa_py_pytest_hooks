import pytest


def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    parser.addoption(
        "--browser",
        choices=['chrome', 'firefox'],
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config: pytest.Config):
    if config.getoption("--mobile-only") and config.getoption("--browser") == 'firefox':
        raise ValueError("Нет мобильных тестов на Firefox")