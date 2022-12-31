from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

        # filling address line-1
        address_line_1 = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
        address_line_1.send_keys("1/123,")

        # filling address line-2
        address_line_2 = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input')
        address_line_2.send_keys("john street")

        # Entering city
        city = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input')
        city.send_keys("Chennai")

        # Entering State
        state = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input')
        state.send_keys("Tamil nadu")

        # Entering postal code
        postal_code = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input')
        postal_code.send_keys("600001")

        # Selecting Country

        country = driver.find_element(By.XPATH,'//label[text()="Country"]/following::div[1]')
        country.click()
        time.sleep(15)

        # Entering home number
        home_number = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input')
        home_number.send_keys("22334455")

        # Entering mobile number
        mobile_number = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
        mobile_number.send_keys("9876543210")

        # Entering work number
        work_number = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input')
        work_number.send_keys("33442211")

        # Entering work email
        work_email = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input')
        work_email.send_keys("projectAT@example.com")

        # Entering other email
        other_email = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input')
        other_email.send_keys("example@project.com")

        # Clicking Save button
        savee_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        savee_button.click()
        time.sleep(2)



af=orangehrm()
af.test()