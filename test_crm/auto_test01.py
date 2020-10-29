import re
import time
from selenium import webdriver
driver=webdriver.Chrome('C:\\Program Files\\python\\python37\\chromedriver.exe')
# driver.get('https://www.baidu.com/')
#窗口最大化
# driver.maximize_window()
# time.sleep(3)
#设置windo窗体
# driver.set_window_size(400,600)
#返回
# driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys('sa')
#driver.find_element_by_xpath('//*[@id="su"]').click()
#id定位
# driver.find_element_by_id('kw').send_keys('蜡笔小新')
#name定位
# driver.find_element_by_name('wd').send_keys('蜡笔小新')
#classname定位
# driver.find_element_by_class_name('s_ipt').send_keys('蜡笔小新')
#文本链接
# driver.find_element_by_link_text('新闻').click()
#部分的---》找第一个
# driver.find_element_by_partial_link_text('新')
#路径----xpath
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('sa')
#多元素--->找规律1
# try:
#     for i in (1,7):
#         element=driver.find_element_by_css_selector('//*[@id="s-top-left"]/a['+str(i)+']')
#         print(element.text)
# finally:
#     driver.quit()
#多元素--->找规律2
# try:
#     lst_element=driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')
#     len(lst_element)
#     for element in lst_element:
#         print(element.text)
# finally:
#     driver.quit()
#css
# driver.find_element_by_css_selector('#kw').send_keys('蜡笔小新')
# driver.find_element_by_css_selector('body > input').send_keys('蜡笔小新')
# 标签定位
# list_tag_element=driver.find_elements_by_tag_name('input')
# print(len(list_tag_element))

#返回# list_tag_element[1].click()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.quit()#关闭所有
#driver.close()#关闭标签
class JD:
    def __init__(self):
        pass
    def username_type_error(self):
        try:
            driver.get('file:///C:/Users/leipeng/Desktop/jd_reg/jd_reg/demo.html')
            username_element=driver.find_element_by_id('userName')
            username_element.send_keys('12')
            # print(username_element.get_attribute('placeholder'))
            # print(username_element.text)
            # print(driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text)
            error_image=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
            result_error_info=re.search('error.png',error_image).group()
            # print(result_error_info)
            if result_error_info=='error.png' and driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span')=='格式错误，仅支持汉字、字母、数字、“-”“_”的组合':
                print('pass')
            else:
                print(driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span'))
                print('failed')
        except Exception as e:
            print('unkown error')
            print(e)
        finally:
            driver.quit()
if __name__=='__main__':
    jd=JD()
    jd.username_type_error()

