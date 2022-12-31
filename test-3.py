from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class orangehrm():
    def test(self):

        #Initializing the browser
        driver=webdriver.Chrome()
        base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        #Entering user name
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

        # Adding New employee

        # selecting PIM module

        xpath_to_pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
        clicking_to_pim_module = driver.find_element(By.XPATH, xpath_to_pim_module)
        clicking_to_pim_module.click()
        clicking_add_button = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        clicking_add_button.click()

        # entering first name

        Entering_first_name = driver.find_element(By.NAME, "firstName")
        Entering_first_name.send_keys("vijay")

        # entering middle name

        Entering_middle_name = driver.find_element(By.NAME, "middleName")
        Entering_middle_name.send_keys(" ")

        # entering last name

        Entering_last_name = driver.find_element(By.NAME, "lastName")
        Entering_last_name.send_keys("k")

        # Clicking create login deatail
        create_login_deatails = driver.find_element(By.XPATH,
                                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
        create_login_deatails.click()

        # Creating username
        username = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
        username.send_keys("vijay k")

        # Creating  password
        password = driver.find_element(By.XPATH,
                                       "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input")
        password.send_keys("Project@12345")
        confirm_password = driver.find_element(By.XPATH,
                                               "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input")
        confirm_password.send_keys("Project@12345")

        # Submitting username and password
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit.send_keys(Keys.ENTER)
        time.sleep(5)


ac=orangehrm()
ac.test()