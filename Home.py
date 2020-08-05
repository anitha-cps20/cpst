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

# To add Category
driver.find_element_by_partial_link_text("Category").click()
