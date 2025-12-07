from selenium.webdriver.common.by import By
import time

def test_logout(driver, base_url):
    driver.get(base_url + "/login")

    driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("testuser")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]").click()

    time.sleep(1)

    logout_icon = driver.find_element(By.XPATH, "//*[contains(@class,'cursor-pointer')]")
    logout_icon.click()

    assert "/login" in driver.current_url
