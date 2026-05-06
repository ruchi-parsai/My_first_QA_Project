import random
from playwright.sync_api import expect


class CommonUtils:

    @staticmethod
    def select_random_option(page, option_locator):
        expect(option_locator.first).to_be_visible(timeout=10000)
        count = option_locator.count()

        if count == 0:
            raise Exception("No dropdown options found")

        random_index = random.randint(0, count - 1)
        option_locator.nth(random_index).click()