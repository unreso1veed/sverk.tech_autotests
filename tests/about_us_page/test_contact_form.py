from utils.device_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from urllib.parse import unquote

#TC-AU-1

def test_open_contact_form():
    driver = get_driver()

    try:
        driver.get("https://sverk.tech/about")

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section[3]/div[2]/div/a').click()
        wait = WebDriverWait(driver, 10)

        expected_url = "https://sverk.tech/applicant?source=AboutPage&target=JoinTeam"
        actual_url = unquote(driver.current_url)

        assert expected_url == actual_url, f"Ожидался переход на {expected_url}, фактически перешли на {actual_url}"
        
    finally:
        driver.quit()
