import os
import unittest
import paramunittest
import logging

from utils.Logs import log_init
from utils.excel_reader import readExcel
from utils.request_method import request_Method
from config.config_reader import sys_cfg


log_init()
case_xls = readExcel().get_xls('test_case.xlsx', 'Sheet1')
base_url = sys_cfg['base_url']
logger = logging.getLogger('接口测试')
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@paramunittest.parametrized(*case_xls)
class testApi(unittest.TestCase):
    def setParameters(self, case_name, path, params, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.params = str(params)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        logger.info(self.case_name + "测试开始")

    def test_case(self):
        url = base_url + self.path
        result = request_Method().run_main(self.method, url, self.params)
        logger.info(result)

    def tearDown(self):
        logger.info("测试结束，输出log完结\n\n")
