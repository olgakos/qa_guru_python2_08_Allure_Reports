import allure
import pytest
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 3
    #browser.config.base_url = 'https://github.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield

def test_github_with_allure_step():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label("owner", "olgakos")
    allure.dynamic.description("Description: Github test")
    allure.dynamic.feature("Feature: Allure with Issues")
    allure.dynamic.story("Поиск Issues")
    allure.dynamic.link("https://github.com")

    with allure.step('Открыть стартовую страницу Github'):
        browser.open('https://github.com')

    with allure.step('Найти репозиторий по названию'):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("olgakos/qa_guru_python_2_08_allure_reports")
        s(".header-search-input").submit()

    with allure.step('Перейти в репозиторий'):
        s(by.link_text("olgakos/qa_guru_python_2_08_allure_reports")).click()

    with allure.step('Открыть вкладку Issues'):
        s("#issues-tab").click()

    with allure.step('Убедиться, что есть Issues c названием test2'):
        s(by.partial_text("test2")).should(be.visible)