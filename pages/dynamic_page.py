import allure
from playwright.sync_api import Page, expect

class DynamicPage:
    def __init__(self, page: Page):
        self.page = page
        self.start_button = page.get_by_role("button", name="Start")
        self.finish_text = page.locator("#finish h4")

    @allure.step("Открыть страницу динамической загрузки")
    def navigate(self):
        self.page.goto("/dynamic_loading/1")

    @allure.step("Запустить процесс загрузки")
    def start_loading(self):
        self.start_button.click()

    @allure.step("Дождаться появления текста 'Hello World!'")
    def should_see_hello(self):
        # Увеличиваем ожидание до 10 секунд
        expect(self.finish_text).to_be_visible(timeout=10000)
        expect(self.finish_text).to_have_text("Hello World!")
