from selenium.webdriver.common.alert import Alert


class BrowserOperation:
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,id,content):
        try:
            self.driver.find_element_by_id(id).send_keys(content)
        except Exception as e:
            print(e,'element not found')

    def send_keys_x(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not found')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,' not found')

    def click_element_x(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,' not found')

    def change_window(self,window_name):
        try:
            for window in self.driver.window.hanldes:
                self.driver.switch_to.window(window)
                if self.driver.title == window_name:
                    break
        except Exception as e:
            print(e,'not found winow')


    def get_text(self,xpath):
        try:
            self.text = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'not found')
        return self.text
    def alert_text(self):
        alert=Alert(self.driver)
        alert_text=alert.text
        return  alert_text
    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)
    def execute_script(self,customername):
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.find_element_by_name(customername).clear()
    def clear_customer(self,customer):
        self.driver.find_element_by_name(customer).clear()

