import allure
import pytest
from selene import be, by
from selene.support.shared.jquery_style import s
from .utils import *
from allure_commons.types import Severity

@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 3
    #browser.config.base_url = 'https://github.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield

#var1, где переменные в коде
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos")
@allure.description("Description2: Github test")
@allure.feature("Feature: Allure with decorating")
@allure.story("Decorator")
@allure.link("https://github.com")
def test_github_allure_steps_decorate():
    open_main_page()
    search_repository("olgakos/qa_guru_python_2_08_allure_reports")
    go_to_repository("olgakos/qa_guru_python_2_08_allure_reports")
    go_to_issues()
    check_issue("#2")

@allure.step("Открыть стартовую страницу Github")
def open_main_page():
    open_page("https://github.com")

@allure.step("Найти репозиторий по названию")
def search_repository(name_repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(name_repo)
    s(".header-search-input").submit()

@allure.step("Перейти в репозиторий")
def go_to_repository(name_repo2):
    s(by.link_text(name_repo2)).click()

@allure.step("Открыть вкладку Issues")
def go_to_issues():
    s("#issues-tab").click()

@allure.step("Убедиться, что есть Issues c #2")
def check_issue(name_issues):
    s(by.partial_text(name_issues)).should(be.visible)


# #var2, где переменные вынесены в utils.py (см. import)
@allure.tag("web2")
@allure.severity(Severity.NORMAL)
@allure.label("olgakos2")
@allure.description("Description2: Github test2")
@allure.feature("Feature: Allure with decorating2")
@allure.story("Decorator2")
@allure.link("https://github.com")
def test_github_allure_steps_decorate2():
    open_main_page()
    search_repository(repo_adress)
    go_to_repository(repo_adress)
    go_to_issues()
    check_issue(name)

@allure.step("Открыть стартовую страницу Github2")
def open_main_page():
    open_page(base_url)

@allure.step("Найти репозиторий по названию2")
def search_repository(repo_adress):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo_adress)
    s(".header-search-input").submit()

@allure.step("Перейти в репозиторий2")
def go_to_repository(repo_adress):
    s(by.link_text(repo_adress)).click()

@allure.step("Открыть вкладку Issues2")
def go_to_issues():
    s("#issues-tab").click()

@allure.step("Убедиться, что есть Issues c #2 (2)")
def check_issue(name):
    s(by.partial_text(name)).should(be.visible)