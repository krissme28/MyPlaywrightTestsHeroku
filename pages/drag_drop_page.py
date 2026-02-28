import allure
from playwright.sync_api import Page, expect

class DragDropPage:
    def __init__(self, page: Page):
        self.page = page
        self.column_a = page.locator("#column-a")
        self.column_b = page.locator("#column-b")

    @allure.step("Открыть страницу Drag and Drop")
    def navigate(self):
        self.page.goto("/drag_and_drop")

    @allure.step("Перетащить блок A на блок B")
    def drag_a_to_b(self):
        self.column_a.drag_to(self.column_b)

    @allure.step("Проверить, что в блоке A теперь текст {text}")
    def should_have_text_in_a(self, text):
        expect(self.column_a).to_have_text(text)
