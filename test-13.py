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

        #Clicking on Tax exemptions
        tax_exemptions=driver.find_element(By.XPATH,'//a[text()="Tax Exemptions"]')
        tax_exemptions.click()

        #Selecting status
        status=driver.find_element(By.XPATH,'//label[text()="Status"]/following::div[4]')
        status.click()
        time.sleep(3)

        #selecting status-1
        status_1=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Married"]')
        status_1.click()
        time.sleep(3)


        #Entering Exemptions
        exemptions=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input")
        exemptions.send_keys("22")

        #Selecting state
        state=driver.find_element(By.XPATH,"//label[text()='State']/following::div[4]")
        state.click()
        time.sleep(3)

        #Selecting state-1
        state_1=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="American Samoa"]')
        state_1.click()
        time.sleep(3)

        #Entering Exemptions-2
        exemption_2=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input')
        exemption_2.send_keys("22")
        time.sleep(3)

        #Selecting unemployment state
        unemployment_state=driver.find_element(By.XPATH,'//label[text()="Unemployment State"]/following::div[4]')
        unemployment_state.click()
        time.sleep(3)

        # Selecting unemployment state-1
        unemployment_state_1=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="American Samoa"]')
        unemployment_state_1.click()
        time.sleep(3)

        #Selecting working state
        work_state=driver.find_element(By.XPATH,'//label[text()="Work State"]/following::div[4]')
        work_state.click()
        time.sleep(2)

        # Selecting working state-1
        work_state_1=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Armed Forces Canada"]')
        work_state_1.click()
        time.sleep(3)

        #Clicking save button
        save_button=driver.find_element(By.XPATH,"//button[@type='submit']")
        save_button.click()
        time.sleep(5)


am=orangehrm()
am.test()