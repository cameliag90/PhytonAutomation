import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginPageElements:
    @classmethod
    def setup_class(cls):
        # Setup the WebDriver
        cls.driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
        cls.driver.get('https://www.saucedemo.com/')

    @classmethod
    def teardown_class(cls):
        # Quit the WebDriver
        cls.driver.quit()

    def test_username_field_displayed(self):
        username_field = self.driver.find_element(By.ID, 'user-name')
        assert username_field.is_displayed()
        assert username_field.get_attribute('placeholder') == 'Username'

    def test_password_field_displayed(self):
        password_field = self.driver.find_element(By.ID, 'password')
        assert password_field.is_displayed()
        assert password_field.get_attribute('placeholder') == 'Password'

    def test_login_button_displayed(self):
        login_button = self.driver.find_element(By.ID, 'login-button')
        assert login_button.is_displayed()
        assert login_button.get_attribute('disabled') is None

        # Get the computed style of the login button
        script = "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');"
        background_color = self.driver.execute_script(script, login_button)

        print(f"Login button background color: {background_color}")

        # Make the assertion more robust
        assert background_color is not None, "The computed 'background-color' is None"
        assert background_color == 'rgb(61, 220, 145)', f"Expected 'rgb(61, 220, 145)', but got {background_color}"

    def test_login_credentials_information_dialog(self):
        login_credentials = self.driver.find_element(By.CLASS_NAME, 'login_credentials')
        assert login_credentials.is_displayed()
        text = login_credentials.text
        assert 'Accepted usernames are:' in text
        assert 'standard_user' in text
        assert 'locked_out_user' in text
        assert 'problem_user' in text
        assert 'performance_glitch_user' in text
        assert 'error_user' in text
        assert 'visual_user' in text

        password = self.driver.find_element(By.CLASS_NAME, 'login_password')
        assert password.is_displayed()
        password_text = password.text
        assert 'Password for all users:' in password_text
        assert 'secret_sauce' in password_text

if __name__ == "__main__":
    pytest.main()
