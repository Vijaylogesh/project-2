from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

        # Clicking PIM Module
        xpath_to_pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
        clicking_to_pim_module = driver.find_element(By.XPATH, xpath_to_pim_module)
        time.sleep(3)
        clicking_to_pim_module.click()

        # Searching for employee name
        Employee_name = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        Employee_name.send_keys("vijay k")
        time.sleep(2)

        # Clicking submit button
        search = driver.find_element(By.XPATH, '//button[@type="submit"]')
        search.click()
        time.sleep(2)

        # Click on edit option
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        Edit_option = driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-pencil-fill"]')
        Edit_option.click()

        # Clicking Job tab
        job_tab = driver.find_element(By.XPATH, '//a[text()="Job"]')
        job_tab.click()
        time.sleep(2)

        # xpath to Terminate button
        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(4)

        # xpath to termination date
        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input').send_keys(
            "2022-12-12")
        time.sleep(4)

        # xpath to termination reason
        driver.find_element(By.XPATH, '//label[text()="Termination Reason"]/following::div[3]').click()
        time.sleep(4)

        # xpath to termination reason dropdown
        driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Contract Not Renewed"]').click()
        time.sleep(4)

        # xpath to Note
        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea').send_keys(
            "Nil")
        time.sleep(4)

        # xpath to save
        driver.find_element(By.XPATH, '//label[text()="Note"]/following::button[2]').click()
        time.sleep(7)

        # xpath to activate
        driver.find_element(By.XPATH,
                            '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(7)


ak=orangehrm()
ak.test()
