import allure
import pytest


@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    pass
    # assert request.config.option.browser == 'chrome'
    # if request.config.option.browser == 'chrome':
    #     print("chrome")
    # else:
    #     print("firefox")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", [metafunc.config.getoption("--browser")], indirect=True)

#
# def test_desktop_page(browser, request):
#     allure.dynamic.title(" ".join(request.node.name.split("_")[1:]).capitalize())


def test_mobile_page(browser):
    pass

def test_desktop_page(browser):
    pass