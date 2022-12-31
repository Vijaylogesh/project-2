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

        # Clicking contact deatails
        contact_deatails = driver.find_element(By.XPATH, '//a[text()="Contact Details"]')
        contact_deatails.click()
        time.sleep(2)

        # Clicking Emergency contact
        emergency_contact = driver.find_element(By.XPATH,'//a[text()="Emergency Contacts"]')
        emergency_contact.click()
        time.sleep(2)

        # Clicking Dependents
        dependents = driver.find_element(By.XPATH, '//a[text()="Dependents"]')
        dependents.click()
        time.sleep(2)

        # Clicking immigration tab
        immigration_tab = driver.find_element(By.XPATH, '//a[text()="Immigration"]')
        immigration_tab.click()
        time.sleep(2)

        # Clicking Job tab
        job_tab = driver.find_element(By.XPATH, '//a[text()="Job"]')
        job_tab.click()
        time.sleep(2)

        #Clicking Salary tab
        salary=driver.find_element(By.XPATH,'//a[text()="Salary"]')
        salary.click()
        time.sleep(2)

        #Clicking on Tax exemptions
        tax_exemptions=driver.find_element(By.XPATH,'//a[text()="Tax Exemptions"]')
        tax_exemptions.click()
        time.sleep(2)

        #Clicking on report to
        report_to_tab=driver.find_element(By.XPATH,'//a[text()="Report-to"]')
        report_to_tab.click()
        time.sleep(2)

        #Clicking on Qualifications
        qualification=driver.find_element(By.XPATH,'//a[text()="Qualifications"]')
        qualification.click()
        time.sleep(2)

        #Clicking on membership
        membership=driver.find_element(By.XPATH,'//a[text()="Memberships"]')
        membership.click()
        time.sleep(2)


ad=orangehrm()
ad.test()

