from utils.device_driver import get_driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import unquote

def test_open_telegram():
    driver = get_driver()

    try:
        driver.get("https://sverk.tech")

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/a[1]').click()
        wait = WebDriverWait(driver, 10)
        





    finally:
        driver.quit()
