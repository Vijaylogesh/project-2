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

        # Clicking Job tab
        job_tab = driver.find_element(By.XPATH, '//a[text()="Job"]')
        job_tab.click()
        time.sleep(2)

        #Selecting joining date
        joining_date=driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')

        joining_date.send_keys("2020-10-11")
        time.sleep(2)

        #Selecting job title
        job_catagory=driver.find_element(By.XPATH,"//label[text()='Joined Date']/following::div[7]")
        job_catagory.click()
        driver.implicitly_wait(3)

        #Selecting Job drop down
        job_drop_down=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Software Engineer']")
        job_drop_down.click()

        #Selecting job catagory
        job_catagory=driver.find_element(By.XPATH,"//label[text()='Job Category']/following::div[1]")
        job_catagory.click()

        # drop dowm job category
        category_drop_down=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Technicians']")
        category_drop_down.click()


        #Selecting sub unit
        sub_unit=driver.find_element(By.XPATH,"//label[text()='Sub Unit']/following::div[1]")
        sub_unit.click()
        driver.implicitly_wait(6)

        # drop dowm job category
        sub_drop_down=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Quality Assurance']")
        sub_drop_down.click()

        #Selecting location
        location=driver.find_element(By.XPATH,"//label[text()='Location']/following::div[1]")
        location.click()
        driver.implicitly_wait(3)

        #Selecting location drop down
        location_drop_down=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='New York Sales Office']")
        location_drop_down.click()

        #Selecting employee contract
        employee_contract=driver.find_element(By.XPATH,"//label[text()='Employment Status']/following::div[1]")
        employee_contract.click()
        driver.implicitly_wait(6)

        #dropdown for employee contract
        employee_drop_down =driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Full-Time Permanent']")
        employee_drop_down.click()

        #Toggle employee contract deatails
        employee_contract_deatails=driver.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
        employee_contract_deatails.click()
        driver.implicitly_wait(3)

        #Selecting Employee start date
        start_date=driver.find_element(By.XPATH,"//p[text()='Include Employment Contract Details']/following::input[2]")
        start_date.send_keys("2020-02-22")
        driver.implicitly_wait(3)

        #Selecting Employee end date
        end_date=driver.find_element(By.XPATH,"//p[text()='Include Employment Contract Details']/following::input[3]")
        end_date.send_keys("2022-12-31")
        driver.implicitly_wait(3)
        time.sleep(2)

        #Clicking save button
        save_button=driver.find_element(By.XPATH,'//button[@type="submit"]')
        save_button.click()
        time.sleep(5)





        # Clicking save button
        job_experience_save = driver.find_element(By.XPATH, '//button[@type="submit"]')
        job_experience_save.click()
        time.sleep(5)


aj=orangehrm()
aj.test()