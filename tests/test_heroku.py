import allure
from pages.login_page import LoginPage
from pages.checkbox_page import CheckboxPage
from pages.drag_drop_page import DragDropPage
from pages.alerts_page import AlertsPage
from pages.dynamic_page import DynamicPage


@allure.feature("Авторизация")
def test_login_flow(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.should_be_logged_in()


@allure.feature("Элементы UI")
@allure.story("Чекбоксы")
def test_checkboxes_flow(page):
    checkbox_page = CheckboxPage(page)

    checkbox_page.navigate()
    checkbox_page.set_checkbox(0, True)
    checkbox_page.should_be_checked(0)

@allure.feature("Элементы UI")
def test_drag_and_drop(page):
    dd_page = DragDropPage(page)
    dd_page.navigate()
    dd_page.drag_a_to_b()
    dd_page.should_have_text_in_a("B")

@allure.feature("Интерфейс")
def test_javascript_alerts(page):
    alerts_page = AlertsPage(page)
    alerts_page.navigate()
    alerts_page.accept_alert()
    alerts_page.should_have_result("You successfully clicked an alert")

@allure.feature("Ожидания")
def test_dynamic_loading(page):
    dyn_page = DynamicPage(page)
    dyn_page.navigate()
    dyn_page.start_loading()
    dyn_page.should_see_hello()

