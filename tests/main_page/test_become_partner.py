from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.device_driver import get_driver
from urllib.parse import unquote

#TC-MP-2

def test_order_drone():
    driver = get_driver()
    try:
        driver.get("https://sverk.tech")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section/div/div[1]/div/a[2]').click()
        
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/h1")))

        expected_url = "https://sverk.tech/applicant?source=HomePage&target=Встречающий экран&button=Стать партнером"
        actual_url = unquote(driver.current_url)
        
        assert actual_url == expected_url, f"URL не соответствует ожидаемому: {actual_url}"
        
        print("\033[92mMain page - become partner - passed!\033[0m")

    finally:
        driver.quit()