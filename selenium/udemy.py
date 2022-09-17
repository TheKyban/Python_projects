import time
from selenium.webdriver.common.by import By
from selenium import webdriver
courses = [
    '/html/body/section[1]/div/div[2]/div[2]/form/div[1]/div[10]/div/div[2]/h5/a',
    '/html/body/section[1]/div/div[2]/div[2]/form/div[1]/div[11]/div/div[2]/h5/a',
    '/html/body/section[1]/div/div[2]/div[2]/form/div[1]/div[15]/div/div[2]/h5/a',
    '/html/body/section[1]/div/div[2]/div[2]/form/div[1]/div[25]/div/div[2]/h5/a',
]


chrome_driver_path = "D:\programming\Python Project\selenium\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)



driver.get('https://coursefolder.net/live-free-udemy-coupon.php')
# driver.find_element(By.XPATH, courses[1]).click()
# time.sleep(5)
