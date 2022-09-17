import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_path = "D:\programming\Python Project\selenium\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://tinder.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]').click()
driver.find_element(By.CSS_SELECTOR, "#o-98920890 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div.Mx\(28px\).Mx\(8px\)--m > a").click()
driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/button').click()
driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/span[2]').click()
time.sleep(5)
driver.quit()