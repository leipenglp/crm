import logging
import time


class AutoLog:
    def __init__(self):
        self.logger=logging.getLogger('log')
    def set_mes(self,mess,level_p):
        try:
            now_time = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件handle
            fh = logging.FileHandler('../log_info/auto_' + now_time + '.log')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(levelname)s %(filename)s %(asctime)s %(message)s')
            fh.setFormatter(fm)
            # 对控制台格式化
            ch.setFormatter(fm)
            # 文件句柄加入logger
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输入info
            if level_p=='debug':
                self.logger.debug(mess)
            elif level_p=='info':
                self.logger.info(mess)
            elif level_p=='error':
                self.logger.error(mess)
            self.logger.info('info  message')
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
        except:
            print('file exception')
        finally:
            fh.close()
# if __name__=='__main__':
#     log=AutoLog()
#     url='www.baidu.com'
#     log.set_mes('打开'+url,'info')