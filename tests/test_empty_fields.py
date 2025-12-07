from selenium.webdriver.common.by import By

def test_empty_login_fields(driver, base_url):
    driver.get(base_url + "/login")

    driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]").click()

    assert "required" in driver.page_source.lower()
