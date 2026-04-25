from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.device_driver import get_driver
from urllib.parse import unquote

#TC-MP-1

def test_order_drone():
    driver = get_driver()
    try:
        driver.get("https://sverk.tech")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section/div/div[1]/div/a[1]').click()
        
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/h1")))

        expected_url = "https://sverk.tech/applicant?source=HomePage&target=Встречающий экран&button=Заказать дрон"
        actual_url_decoded = unquote(driver.current_url)
        
        assert actual_url_decoded == expected_url, f"URL не соответсвует: {actual_url_decoded}"
        
        print("\033[92mMain page - drone order - passed!\033[0m")

    finally:
        driver.quit()