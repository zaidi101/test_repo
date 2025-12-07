from selenium.webdriver.common.by import By

def test_invalid_login(driver, base_url):
    driver.get(base_url + "/login")

    driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("wrong")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("wrongpass")

    driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]").click()

    assert "invalid" in driver.page_source.lower() or "error" in driver.page_source.lower()
