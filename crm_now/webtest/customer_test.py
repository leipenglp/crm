import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys


sys.path.append('C:\\Program Files\\python\\python37\\auto_07')

from auto_07.crm_now.base.browseroperation import BrowserOperation
from auto_07.crm_now.webpage.customerpage import CustomerPage
from auto_07.crm_now.base.usebrowser import UseBrowser
from auto_07.crm_now.util.excel_opertation import OperationExcel


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cp = CustomerPage()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.op = OperationExcel('../conifg/test.xlsx', '用例参数')
    def test_customer_add(self):
        self.cp.customer_add(customername=self.op.get_cell(6, 5),customeraddman=self.op.get_cell(6,6),customeremail=self.op.get_cell(6, 7),customerbirthday=self.op.get_cell(6, 8))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text,self.op.get_cell(6, 4))
    def test_customer_modif(self):
        self.cp.customer_modify(customeremail=self.op.get_cell(7, 7))
        alert_text = self.bo.alert_text()
        self.assertEqual(alert_text, self.op.get_cell(7, 4))

    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTest(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../report/report_' + date_now + '.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='ato_test', description='ui_auto_test')
        runner.run(suite)