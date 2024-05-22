import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginWithInvalidCredentials:
    @classmethod
    def setup_class(cls):
        # Setup the WebDriver
        cls.driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
        cls.driver.get('https://www.saucedemo.com/')
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.username_field = cls.wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        cls.password_field = cls.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        cls.login_button = cls.wait.until(EC.presence_of_element_located((By.ID, 'login-button')))

    @classmethod
    def teardown_class(cls):
        # Quit the WebDriver
        cls.driver.quit()

    def test_login_with_invalid_username(self):
        self.username_field.send_keys('locked_out_user')
        self.password_field.send_keys('secret_sauce')
        self.login_button.click()

        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error-message-container')))
        assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'

        error_button = self.driver.find_element(By.CLASS_NAME, 'error-button')
        assert error_button.is_displayed()

        error_icons = self.driver.find_elements(By.CLASS_NAME, 'error_icon')
        assert len(error_icons) == 2
        for icon in error_icons:
            assert icon.is_displayed()

        assert self.username_field.get_attribute('value') == 'locked_out_user'
        assert self.password_field.get_attribute('value') == 'secret_sauce'

        error_button.click()
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'h3')))

        assert len(self.driver.find_elements(By.CSS_SELECTOR, 'h3')) == 0
        assert len(self.driver.find_elements(By.CLASS_NAME, 'error_icon')) == 0



if __name__ == "__main__":
    pytest.main()
