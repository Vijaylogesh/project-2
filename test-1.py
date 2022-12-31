from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class orangehrm():
    def test(self):
        # Initializing the browser
        driver = webdriver.Chrome()
        base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        # Entering user name
        Xpath_to_username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        Entering_username = driver.find_element(By.XPATH, Xpath_to_username)
        Entering_username.click()
        Entering_username.send_keys("Admin")

        # Entering password
        Xpath_to_password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        Entering_password = driver.find_element(By.XPATH, Xpath_to_password)
        Entering_password.click()
        Entering_password.send_keys("admin123")

        # logging to orangeHRM
        Entering_password.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)

        # Clicking for search tab
        search_tab = driver.find_element(By.XPATH, '//input[@class="oxd-input oxd-input--active"]')

        search_list=['Admin','Pim','Leave','Time','Recruitment','My info','Performance','Dashboard','Directory','Maintenance','Buzz']

        # Searching in uppercase
        for a in search_list:
            search_tab.send_keys(a.upper())
            time.sleep(1)

    #clearing the exiting text
            search_tab.send_keys(Keys.CONTROL, 'a')
            search_tab.send_keys(Keys.BACKSPACE)
            time.sleep(1)

        # Searching in lower case
            search_tab.send_keys(a.lower())
            time.sleep(1)

            # clearing the exiting text
            search_tab.send_keys(Keys.CONTROL, 'a')
            search_tab.send_keys(Keys.BACKSPACE)

        driver.close()


aa = orangehrm()
aa.test()
