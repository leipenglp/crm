from selenium import webdriver


class UseBrowser:

    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        UseBrowser.driver = self.driver


    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()