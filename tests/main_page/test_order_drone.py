import requests
import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_order_drone():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://sverk.tech")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/section/div/div[1]/div/a[1]').click()
        
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/h1")))
        
        print("\033[92mMain page - drone order - passed!\033[0m")

    finally:
        driver.quit()