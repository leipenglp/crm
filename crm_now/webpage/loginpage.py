from auto_07.crm_now.base.browseroperation import BrowserOperation
from auto_07.crm_now.base.usebrowser import UseBrowser
from auto_07.crm_now.conifg.log_crm import AutoLog


class LoginPage:

    def __init__(self):
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://localhost:8080/crm')
        self.log = AutoLog()
    def login(self,username,password):
        # self.log.set_mes('---登录功能开始---', 'info')
        self.bo.send_keys_x('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input',username)
        self.log.set_mes('-输入用户名-', 'info')
        self.bo.send_keys_x('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input',password)
        self.log.set_mes('-登输入密码-', 'info')
        self.bo.click_element('//*[@id="in1"]')
        self.log.set_mes('-点击登录-', 'info')

    def login_correct_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)
        return self.bo.get_text(xpath)