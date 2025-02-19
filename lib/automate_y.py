from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
# Initialize the WebDriver and other settings
email="azizwerghighi@gmail.com"
password="12312300aziz@A"
base_url = "https://www.youtube.com/"
def authenticate_user(email, password, base_url):
    options = uc.ChromeOptions()
    options.user_data_dir = "c:\\temp\\profile"
    driver = uc.Chrome(
    options = options 
    )  
    driver.delete_all_cookies()
    driver.get(base_url)

    connexion= WebDriverWait(
    driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')))
    connexion.click()
    try:
        identifiant= WebDriverWait(
        driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
        identifiant.send_keys(email)
        suivant= WebDriverWait(
    driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')))
        ActionChains(driver).move_to_element(suivant).click(suivant).perform()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
        email_exist=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]')
        if email_exist:
            print("Email already exists")
            ActionChains(driver).move_to_element(email_exist).click(email_exist).perform()
 

    time.sleep(10)
    password= driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    login= WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')))
    ActionChains(driver).move_to_element(login).click(login).perform()
    time.sleep(10)
    return driver

driver = authenticate_user(email, password, base_url)

driver.quit()
    
    