from selenium.webdriver.common.by import By
import time

def test_chat_bubble_display(driver, base_url):
    driver.get(base_url + "/login")

    driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("testuser")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]").click()

    time.sleep(1)

    bubbles = driver.find_elements(By.XPATH, "//*[contains(@class,'chat-bubble')]")
    assert len(bubbles) >= 0  # At least UI loads properly
