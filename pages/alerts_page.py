import allure
from playwright.sync_api import Page, expect

class AlertsPage:
    def __init__(self, page: Page):
        self.page = page
        self.result_text = page.locator("#result")

    @allure.step("Открыть страницу алертов")
    def navigate(self):
        self.page.goto("/javascript_alerts")

    @allure.step("Нажать на кнопку и подтвердить алерт")
    def accept_alert(self):
        # Настраиваем обработчик ДО клика
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Click for JS Alert").click()

    @allure.step("Проверить текст результата")
    def should_have_result(self, text):
        expect(self.result_text).to_have_text(text)
