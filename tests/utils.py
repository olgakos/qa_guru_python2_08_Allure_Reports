from selene.support.shared import browser

base_url = "https://github.com"
repo_adress = "olgakos/qa_guru_python_2_08_allure_reports"
name = "#2"

def open_page(url):
    browser.open(url)