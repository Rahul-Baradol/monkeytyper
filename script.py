from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=opts)

# Navigate to a website
driver.get("https://monkeytype.com/")

sleep(2)

modes = driver.find_elements(By.CSS_SELECTOR, "div.textButton")
modes[3].click()

sleep(2)
modes[13].click()

sleep(2)

words = driver.find_elements(By.CSS_SELECTOR, "div.word")

actions = ActionChains(driver)

for word in words:
   letters = word.find_elements("xpath", "./*")

   for letter in letters:
      character = letter.text
    
      actions.send_keys(character)
      actions.pause(0.01)

   actions.send_keys(" ")
   actions.pause(0.01)

actions.perform()

sleep(10)
driver.quit()