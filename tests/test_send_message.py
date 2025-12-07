from selenium.webdriver.common.by import By
import time

def login(driver, base_url):
    driver.get(base_url + "/login")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("testuser")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-block')]").click()

def test_send_message(driver, base_url):
    login(driver, base_url)

    message_input = driver.find_element(By.XPATH, "//input[@placeholder='Send a message']")
    message_input.send_keys("Hello test message")

    send_btn = driver.find_element(By.XPATH, "//button[contains(@class,'items-center')]")
    send_btn.click()

    time.sleep(1)

    bubbles = driver.find_elements(By.XPATH, "//*[contains(@class,'chat-bubble')]")
    assert any("Hello test message" in b.text for b in bubbles)

