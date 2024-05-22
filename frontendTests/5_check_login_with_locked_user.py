import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()


def test_locked_username(driver):
    # Navigate to the login page
    driver.get('https://www.saucedemo.com/')

    # Find elements and perform login
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_field.send_keys('locked_out_user')
    password_field.send_keys('secret_sauce')
    login_button.click()

    # Check error message
    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container')))
    assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'

    # Check error icons
    error_icons = driver.find_elements(By.CLASS_NAME, 'error_icon')
    assert len(error_icons) == 2
    for icon in error_icons:
        assert icon.is_displayed()

    # Check entered values
    assert username_field.get_attribute('value') == 'locked_out_user'
    assert password_field.get_attribute('value') == 'secret_sauce'

    # Dismiss error message and icons
    error_button = driver.find_element(By.CLASS_NAME, 'error-button')
    error_button.click()

    # Wait for error message to disappear
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'h3')))

    # Check that error message and icons are no longer displayed
    assert not driver.find_elements(By.CSS_SELECTOR, 'h3')
    assert not driver.find_elements(By.CLASS_NAME, 'error_icon')

if __name__ == "__main__":
    pytest.main()
