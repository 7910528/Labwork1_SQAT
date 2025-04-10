from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LipsumPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://lipsum.com/"
        self.ukrainian_link = (By.XPATH, "//a[text()='Українська']")
        self.text_area = (By.XPATH, "//div[@id='Panes']")

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState == 'complete'")
        )

    def switch_to_ukrainian(self):
        wait = WebDriverWait(self.driver, 15)
        ukrainian_link_element = wait.until(EC.element_to_be_clickable(self.ukrainian_link))
        ukrainian_link_element.click()

    def get_generated_text(self):
        wait = WebDriverWait(self.driver, 10)
        text_area_element = wait.until(EC.visibility_of_element_located(self.text_area))
        return text_area_element.text
