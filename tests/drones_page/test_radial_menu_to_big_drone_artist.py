from utils.device_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from urllib.parse import unquote

#TC-D-2

def test_radial_menu_to_big_artist_drone():
    driver = get_driver()
    try:
        driver.get('https://sverk.tech/drones/educational-drone')
        
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section/div/section[1]/div/div/div[2]/div[1]/button[1]').click()
        wait = WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section/div/section[1]/div/div/div[1]/div[2]/a').click()
        wait = WebDriverWait(driver, 10)

        expected_url = 'https://sverk.tech/drones/big-drone-artist'
        actual_url = unquote(driver.current_url)    

        assert expected_url == actual_url, f"Ожидался переход на {expected_url}, перешли на {actual_url}"
        
    finally:
        driver.quit()