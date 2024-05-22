import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginWithValidCredentials:
    @classmethod
    def setup_class(cls):
        # Setup the WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.saucedemo.com/')

    @classmethod
    def teardown_class(cls):
        # Quit the WebDriver
        cls.driver.quit()

    def test_login_successfully_with_valid_credentials(self):
        # Create a new wait instance with a timeout of 20 seconds
        wait = WebDriverWait(self.driver, 20)

        # Wait until the elements are found and store them
        username_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

        # Enter credentials and click login
        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')
        login_button.click()

        # Wait until the URL changes to the inventory page
        wait.until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))

        # Check if the current URL is correct
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'


if __name__ == "__main__":
    pytest.main()
