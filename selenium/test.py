import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

chrome_driver_path = "D:\programming\Python Project\selenium\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.implicitly_wait(5)
driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")
text = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/main/div/p[4]/a").click()
time.sleep(2)
driver.switch_to.alert.dismiss()

driver.quit()
