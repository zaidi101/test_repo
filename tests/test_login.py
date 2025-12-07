from selenium.webdriver.common.by import By

def test_login_page_load(driver, base_url):
    driver.get(base_url + "/login")
    assert "Login" in driver.page_source


def test_login_valid_credentials(driver, base_url):
    driver.get(base_url + "/login")

    # Email field = first input with placeholder "Enter username"
    username = driver.find_element(By.XPATH, "//input[@placeholder='Enter username']")
    username.send_keys("testuser")

    password = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    password.send_keys("password123")

    login_btn = driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]")
    login_btn.click()

    assert "/chat" in driver.current_url
