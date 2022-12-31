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

        #Clicking on salary tab
        salary_tab=driver.find_element(By.XPATH,'//a[text()="Salary"]')
        salary_tab.click()

        #Clicking on add button
        add_button=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button')
        add_button.click()

        #Filling salary component
        salary_component=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
        salary_component.send_keys("CTC")
        time.sleep(7)

        #Selecting pay grade
        pay_grade = driver.find_element(By.XPATH, '//label[text()="Pay Grade"]/following::div[4]')
        pay_grade.click()
        # Clicking on Pay grade
        clicking_on_pay_grade = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Grade 1"]')
        clicking_on_pay_grade.click()
        time.sleep(3)
        # Xpath for Pay Frequency
        pay_frequency = driver.find_element(By.XPATH, '//label[text()="Pay Frequency"]/following::div[4]')
        pay_frequency.click()

        # Clicking on Pay Frequency

        clicking_on_pay_frequency = driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Hourly"]')
        clicking_on_pay_frequency.click()
        time.sleep(3)

        # Xpath for Currency

        currency_frequency = driver.find_element(By.XPATH,'//label[text()="Currency"]/following::div[4]')
        currency_frequency.click()
        time.sleep(3)

        # Clicking on Currency

        clicking_on_currency = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="United States Dollar"]')
        clicking_on_currency.click()
        time.sleep(3)

        #Entering amount
        amount=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input')
        amount.send_keys("55000")

        #Entering comments
        comments=driver.find_element(By.XPATH,'//textarea[@class="oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical"]')
        comments.send_keys("nil")
        time.sleep(2)




al=orangehrm()
al.test()