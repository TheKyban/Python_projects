from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

twitter_username = "adityakumar5544332211@gmail.com"
twitter_pass = "kumaraditya1392"
twitter_client_id = "QjV4UVl3VTJnZkhZUUFNc1c0blk6MTpjaQ"
twitter_client_secret_id = "aHIypPege0nNv2eehq0Ai0iQiVoDyVPcr2nuKeasEJxS9UtE0z"
twitter_bearer_code = "AAAAAAAAAAAAAAAAAAAAADn5gwEAAAAAyI826hICDvV5pe6qP%2FflC9upgkM%3DbnjPpmWfM2oIqCfFBdM6ApryBGjH0gzfPn2dxV5v0w2HjKCGZJ"
# download = 
# upload = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
class TwitterBot:
    def __init__(self) -> None:
        self.chrome_path = "D:\programming\Python Project\selenium\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_path)
    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, "onetrust-close-btn-container").click()
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)
        self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    def twitter(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(twitter_username)
        time.sleep(5)

        next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(twitter_pass)
        time.sleep(5)
        submit = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
        time.sleep(5)
        go_it_prompt = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/span/span').click()

        time.sleep(30)
bot = TwitterBot()
bot.get_speed()
print(f"Download: {bot.download}\nUpload: {bot.upload}")