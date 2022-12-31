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
        driver.implicitly_wait(3)


        #clicking to admin tab
        admin_tab=driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]')
        admin_tab.click()

        #clicking user management
        user_management=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
        user_management.click()
        time.sleep(2)

        #clicking users
        a = ActionChains(driver)
        m = driver.find_element(By.LINK_TEXT,"Users")
        a.move_to_element(m).perform()
        time.sleep(2)

        # select on user role
        select_the_use_role1 = driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[1]")
        ActionChains(driver).move_to_element(select_the_use_role1).click().perform()

        # drop down to admin
        drop_down_for_admin1 = driver.find_element(By.XPATH, '//div[@role="option"]/span[text()="Admin"]')
        ActionChains(driver).move_to_element(drop_down_for_admin1).click().perform()

        # select the status option
        select_the_status1 = driver.find_element(By.XPATH,"//label[text()='Status']/following::div[1]")
        ActionChains(driver).move_to_element(select_the_status1).click().perform()


        drop_down_for_enable1 = driver.find_element(By.XPATH, '//div[@role="option"]/span[text()="Enabled"]')
        ActionChains(driver).move_to_element(drop_down_for_enable1).click().perform()
        time.sleep(5)


        # select on user role On ESS path
        select_the_ESS1 = driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[1]")
        ActionChains(driver).move_to_element(select_the_ESS1).click().perform()

        # drop down to admin
        drop_down_for_ESS1 = driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="ESS"]' )
        ActionChains(driver).move_to_element(drop_down_for_ESS1).click().perform()


        # select the status option
        select_the_status_on_disable1 = driver.find_element(By.XPATH, "//label[text()='Status']/following::div[1]")
        ActionChains(driver).move_to_element(select_the_status_on_disable1).click().perform()
        drop_down_for_disabled = driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Disabled"]')
        ActionChains(driver).move_to_element(drop_down_for_disabled).click().perform()

        time.sleep(5)









ab=orangehrm()
ab.test()