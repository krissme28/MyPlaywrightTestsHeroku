import allure
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Локаторы (описываем их один раз)
        self.username_field = page.get_by_label("Username")
        self.password_field = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name=" Login")
        self.flash_message = page.locator("#flash")

    @allure.step("Открыть страницу логина")
    def navigate(self):
        self.page.goto("/login")

    @allure.step("Авторизоваться с логином {user}")
    def login(self, user, password):
        self.username_field.fill(user)
        self.password_field.fill(password)
        self.login_button.click()

    @allure.step("Проверить сообщение об успехе")
    def should_be_logged_in(self):
        expect(self.flash_message).to_contain_text("You logged into a secure area!")

