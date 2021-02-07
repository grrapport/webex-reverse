import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

test_webex = "https://www.webex.com/test-meeting.html"


chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')

# setting up test meeting
driver.get("https://www.webex.com/test-meeting.html")
driver.find_element(By.ID, "full-name").send_keys("Gerard Kensington")
driver.find_element(By.ID, "email-address").send_keys("gkens@actionchaser.com")
driver.find_element(By.CSS_SELECTOR, ".form_button").click()
time.sleep(4)
driver.find_element(By.ID, "push_download_webapp_buttom_join_link").click()
driver.find_element(By.CSS_SELECTOR, ".style-arrow-2f8xt > .style-icon-2HDxh").click()
element = webdriver.find_element(By.CSS_SELECTOR, ".style-arrow-2f8xt > .style-icon-2HDxh")
actions = webdriver.ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = webdriver.ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.CSS_SELECTOR, "li:nth-child(3)").click()
driver.find_element(By.ID, "interstitial_join_btn").click()

"""
<a id="push_download_webapp_buttom_join_link" href="javascript:void(0);">Join from your browser</a>

"""



