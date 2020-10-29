import time

from auto_07.crm_now.webpage.loginpage import LoginPage
from auto_07.crm_now.util.excel_opertation import OperationExcel
from auto_07.crm_now.conifg.log_crm import AutoLog


class CustomerPage:

    def __init__(self):
        self.login_p = LoginPage()
        self.op = OperationExcel('../conifg/test.xlsx', '用例参数')
        self.login_p.login(self.op.get_cell(5, 2),int(self.op.get_cell(5,3)))
        self.log = AutoLog()
    def customer_add(self,**kwargs):
        self.log.set_mes('-登录成功-', 'info')
        self.login_p.bo.change_frame('topFrame')
        self.login_p.bo.click_element_x('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')
        self.log.set_mes('-点击客户信息-', 'info')
        self.login_p.bo.change_frame('mainFrame')
        self.login_p.bo.click_element_x('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input')
        self.log.set_mes('-登点击添加-', 'info')
        self.login_p.bo.change_frame('mainFrame')
        self.login_p.bo.send_keys_x('/html/body/form/table[1]/tbody/tr[2]/td[2]/input',kwargs.get('customername',''))
        self.log.set_mes('-输入客户姓名-', 'info')
        self.login_p.bo.send_keys_x('/html/body/form/table[1]/tbody/tr[8]/td[2]/input',kwargs.get('customeraddman',''))
        self.log.set_mes('-输入创建人-', 'info')
        self.login_p.bo.send_keys_x('/html/body/form/table[1]/tbody/tr[4]/td[4]/input',kwargs.get('customeremail',''))
        self.log.set_mes('-输入email-', 'info')
        self.login_p.bo.execute_script('customerBirthday')
        self.login_p.bo.send_keys_x('//*[@id="customerBirthday"]',kwargs.get('customerbirthday',''))
        self.log.set_mes('-输入日期-', 'info')
        self.login_p.bo.click_element_x('/html/body/form/table[2]/tbody/tr/td[2]/input')
        self.log.set_mes('-点击提交-', 'info')
    def customer_modify(self,**kwargs):
        self.login_p.bo.change_frame('topFrame')
        self.login_p.bo.click_element_x('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')
        self.log.set_mes('-点击客户信息-', 'info')
        self.login_p.bo.change_frame('mainFrame')
        self.login_p.bo.click_element_x('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[13]/div/span/a[1]')
        self.log.set_mes('-点击编辑-', 'info')
        self.login_p.bo.change_frame('mainFrame')
        self.login_p.bo.clear_customer('customerEmail')
        self.login_p.bo.send_keys_x('/html/body/form/table[1]/tbody/tr[7]/td[2]/input', kwargs.get('customeremail', ''))
        self.log.set_mes('-输入email-', 'info')
        self.login_p.bo.click_element_x('/html/body/form/table[2]/tbody/tr/td[2]/input')
        self.log.set_mes('-点击提交-', 'info')
    def get_add_success_text(self):
        self.login_p.bo.change_window('添加记录成功')
        add_success_text = self.login_p.bo.get_text('/html/boby/center')
        return add_success_text