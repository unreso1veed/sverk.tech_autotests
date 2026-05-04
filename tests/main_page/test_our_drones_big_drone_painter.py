from utils.device_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from urllib.parse import unquote

#TC-MP-5

def test_open_our_drones_big_painter():
    driver = get_driver()

    try:
        driver.get('https://sverk.tech')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[3]/div/div[2]/div[2]/div[1]/button[1]').click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[3]/div/div[2]/div[1]/div[2]/a')))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[3]/div/div[2]/div[1]/div[2]/a').click()

        expected_url = "https://sverk.tech/drones/big-drone-artist"
        actual_url = unquote(driver.current_url)    

        assert expected_url == actual_url, f"URL не соответствует {expected_url}, переход не осуществлен или осуществлен по неверному адресу"

    finally:
        driver.quit()