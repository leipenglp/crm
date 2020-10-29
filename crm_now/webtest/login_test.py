import time
import unittest
import sys


sys.path.append('C:\\Program Files\\python\\python37\\auto_07')
from HTMLTestRunner import HTMLTestRunner

from auto_07.crm_now.webpage.loginpage import LoginPage
from auto_07.crm_now.base.browseroperation import BrowserOperation
from auto_07.crm_now.base.usebrowser import UseBrowser
from auto_07.crm_now.util.excel_opertation import OperationExcel


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.login = LoginPage()
        self.op=OperationExcel('../conifg/test.xlsx','用例参数')
        self.bo = BrowserOperation(UseBrowser.driver)
    def test_login_username_password_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text,self.op.get_cell(1,4))
    def test_login_user_null(self):
        self.login.login(self.op.get_cell(2, 2),self.op.get_cell(2,3))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text,self.op.get_cell(2, 4))
    def test_login_pass_null(self):
        self.login.login(self.op.get_cell(3,2),self.op.get_cell(3,3))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text,self.op.get_cell(3, 4))
    def test_login_user_pass_error(self):
        self.login.login(self.op.get_cell(4, 2),int(self.op.get_cell(4,3)))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text,self.op.get_cell(4, 4))
    def test_login_success(self):
        self.login.login(self.op.get_cell(5, 2),int(self.op.get_cell(5,3)))
        correct_text = self.login.login_correct_text('topFrame','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
        self.assertEqual(correct_text,self.op.get_cell(5, 4))
    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTest(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='ato_test', description='ui_auto_test')
        runner.run(suite)