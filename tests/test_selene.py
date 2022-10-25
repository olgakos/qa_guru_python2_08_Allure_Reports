import pytest
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

#var1, где данные в коде
def test_github_selene():
    browser.open("https://github.com")
    s(".header-search-input").click()
    s(".header-search-input").send_keys("olgakos/qa_guru_python_2_08_allure_reports")
    s(".header-search-input").submit()
    s(by.link_text("olgakos/qa_guru_python_2_08_allure_reports")).click()
    s("#issues-tab").click()
    s(by.partial_text("#2")).should(be.visible)

#var2, где данные вынесены в переменные
base_url = "https://github.com"
repo_adress = "olgakos/qa_guru_python_2_08_allure_reports"
name = "#2"
def test_github_selene2():
        browser.open(base_url)
        s(".header-search-input").click()
        s(".header-search-input").send_keys(repo_adress)
        s(".header-search-input").submit()
        s(by.link_text(repo_adress)).click()
        s("#issues-tab").click()
        s(by.partial_text(name)).should(be.visible)