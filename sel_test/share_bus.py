

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# serv_obj = Service("c:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(options=options)
driver.get("https://test.sharebus.co/")
sign_button=driver.find_element(By.XPATH, "//button[text()='Sign in ']")
sign_button.click()
driver.find_element(By.ID, "email").send_keys("brainstation23@yopmail.com")
driver.find_element(By.ID, "password").send_keys("Pass@1234")
sign_button2=driver.find_element(By.XPATH, "//button[text()='Sign in']")
sign_button2.click()
driver.implicitly_wait(10)
#driver.find_element(By.XPATH, "//*[contains(@class,'p-dropdown')]/span[contains(@class,'p-dropdown-label')]").click()
joiner = driver.find_element(By.CSS_SELECTOR, "div.p-dropdown")
joiner.click()
sharelead = driver.find_element(By.XPATH, "//span[text()='Sharelead']")
sharelead.click()
driver.find_element(By.XPATH, "//button/span[text()='Continue']").click()
driver.implicitly_wait(5)

set_up = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/button")
set_up.click()

from_fill = driver.find_element(By.ID, "startPoint").send_keys("Oslo, Norway")
dst_fill = driver.find_element(By.ID, "destination").send_keys("Kolbotn, Norway")

date_fill = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Departure Date']")
date_fill.click()
select_dt = driver.find_element(By.XPATH, "//span[text()=25]")
select_dt.click()







