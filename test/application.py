from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Application:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
        #self.options.add_argument("--disable-blink-features=AutomationControlled")
        #self.options.add_argument("--headless")
        self.driver = webdriver.Chrome('C:/Users/Nate/Desktop/Python/pytest/chromedriver.exe',  options=self.options)
        self.driver.implicitly_wait(30)
        self.vars = {}

    def open_page(self):
        driver = self.driver
        driver.get("https://test.i-smet.kz/")
        driver.maximize_window()

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Вход").click()
        driver.find_element(By.CSS_SELECTOR, ".in-page-wide-content-wrapper").click()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password-log").send_keys(password)
        driver.find_element(By.ID, "kc-login").click()

    def search(self, element):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, ".new.py-top-search > .new.py-search").click()
        driver.find_element(By.CSS_SELECTOR, ".form-control").click()
        driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys(element)
        driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys(Keys.ENTER)

    def destroy(self):
        self.driver.quit()


# self.options = webdriver.ChromeOptions()
#         self.options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
#         self.options.add_argument("--disable-blink-features=AutomationControlled")
#         self.options.add_argument("--headless")
#         self.driver = webdriver.Chrome('C:/Users/Nate/Desktop/Python/pytest/chromedriver.exe',  options=self.options)
