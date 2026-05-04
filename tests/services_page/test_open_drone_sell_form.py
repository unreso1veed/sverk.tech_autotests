from utils.device_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from urllib.parse import unquote

#TC-S-1

def test_open_drone_sell_form():
    driver = get_driver()

    try:
        driver.get('https://sverk.tech/services#sales')

        sell_drone_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sales"]/div[2]/div[1]/div/a'))
        )
        href = sell_drone_link.get_attribute("href")

        assert href == "https://t.me/sverk_official", f"Ожидалась ссылка https://t.me/sverk_official, получена {href}"
        
    finally:
        driver.quit()