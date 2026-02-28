import allure
from playwright.sync_api import Page, expect

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkboxes = page.get_by_role("checkbox")

    @allure.step("Открыть страницу чекбоксов")
    def navigate(self):
        self.page.goto("/checkboxes")

    @allure.step("Установить состояние чекбокса №{index}")
    def set_checkbox(self, index: int, state: bool):
        checkbox = self.checkboxes.nth(index)
        if state:
            checkbox.check()
        else:
            checkbox.uncheck()

    @allure.step("Проверить, что чекбокс №{index} отмечен")
    def should_be_checked(self, index: int):
        expect(self.checkboxes.nth(index)).to_be_checked()
