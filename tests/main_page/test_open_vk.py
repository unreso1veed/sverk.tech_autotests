from utils.device_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

#TC-MP-4

def test_open_vk():
    driver = get_driver()

    try:
        driver.get("https://sverk.tech")

        vk_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/a[2]'))
        )
        href = vk_link.get_attribute("href")

        assert href == "https://vk.com/sverk_official", f"Ожидалась ссылка https://vk.com/sverk_official, получена {href}"

    finally:
        driver.quit()