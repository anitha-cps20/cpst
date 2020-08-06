from selenium import webdriver
import time


class ClinicalIntervention_test():
    # To Setup driver & Launch Application
    def test_setup(self):
        global driver
        driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
        driver.implicitly_wait(3)
        driver.maximize_window()
        time.sleep(5)

        # Open the application
        driver.get("https://qa-telemanage.cpstelepharmacy.com/")
        print(driver.title)
        time.sleep(20)
        print("Home page displays")
        time.sleep(30)

    def addCategory(self):
        # To add Category
        driver.find_element_by_xpath("//img[@src='../../../assets/images/logo.png']").is_displayed()
        print("Displays")
        driver.find_element_by_xpath("(//span[contains(@class,'mat-button-wrapper')])[6]").click()
        driver.find_element_by_xpath("//button[contains(.,'Add New Category')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[contains(@id,'txtname')]").send_keys("test852020")
        time.sleep(5)

