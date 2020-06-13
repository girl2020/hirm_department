# 定义测试类
# 导包
import logging
import unittest
from parameterized import parameterized
import app
from api.departures import DepartmentApi, LoginApi
from utils import read_dep_data


# 定义测试类
class TestDepartment(unittest.TestCase):
    # 定义初始化fixture
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        # 实例化封装的部门接口
        self.dep_api = DepartmentApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 调用封装好的登录的接口发送登录接口请求
        response_login = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                              {"Content-Type": "Application/json"})

        # 打印登录结果
        logging.info("返回的结果为: {}".format(response_login.json()))
        # 提取登录后的令牌
        token = "Bearer " + response_login.json().get("data")
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量的请求头为: {}".format(app.HEADERS))
        # 断言
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(True, response_login.json().get("success"))
        self.assertEqual(10000, response_login.json().get("code"))
        self.assertEqual("操作成功！", response_login.json().get("message"))

    # 定义员工模块的文件路径
    file_path = app.BASE_DIR + "/data/dep.json"

    # 实现添加员工的接口
    # 参数化
    @parameterized.expand(read_dep_data(file_path, "add_dep"))
    def test02_add_dep(self, name, dep_code, success, code, message, http_code):
        # 调用封装好的员工的接口发送添加员工接口请求
        response_add = self.dep_api.add_dep(name, dep_code, app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加部门的结果为: {}".format(response_add.json()))
        # 提取添加员工中的id保存到全局变量中
        app.EMP_ID = response_add.json().get("data").get("id")
        # 打印保存导全局变量中的id
        logging.info("保存到全局变量中的id为: {}".format(app.EMP_ID))
        # 断言
        self.assertEqual(http_code, response_add.status_code)
        self.assertEqual(success, response_add.json().get("success"))
        self.assertEqual(code, response_add.json().get("code"))
        self.assertIn(message, response_add.json().get("message"))

    # 实现查询员工的接口
    # 参数化
    @parameterized.expand(read_dep_data(file_path, "select_dep"))
    def test03_select_dep(self, success, code, message, http_code):
        # 调用封装好的部门的接口发送查询员工接口请求
        response_select = self.dep_api.select_dep(app.EMP_ID, app.HEADERS)
        # 打印查询员工的结果
        logging.info("查询部门的结果为: {}".format(response_select.json()))
        # 断言
        self.assertEqual(http_code, response_select.status_code)
        self.assertEqual(success, response_select.json().get("success"))
        self.assertEqual(code, response_select.json().get("code"))
        self.assertIn(message, response_select.json().get("message"))

    # 实现修改员工的接口
    # 参数化
    @parameterized.expand(read_dep_data(file_path, "modify_dep"))
    def test04_modify_emp(self, name, success, code, message, http_code):
        # 调用封装好的部门的接口发送修改员工接口请求
        response_modify = self.dep_api.modify_dep({"name": name}, app.EMP_ID, app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改部门的结果为: {}".format(response_modify.json()))
        # 断言
        self.assertEqual(http_code, response_modify.status_code)
        self.assertEqual(success, response_modify.json().get("success"))
        self.assertEqual(code, response_modify.json().get("code"))
        self.assertIn(message, response_modify.json().get("message"))

    # 实现删除员工的接口
    # 参数化
    @parameterized.expand(read_dep_data(file_path, "delete_dep"))
    def test05_delete_emp(self,success, code, message, http_code):
        # 调用封装好的部门]的接口发送删除员工接口请求
        delete_modify = self.dep_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印删除员工的结果
        logging.info("删除部门的结果为: {}".format(delete_modify.json()))
        # 断言
        self.assertEqual(http_code, delete_modify.status_code)
        self.assertEqual(success, delete_modify.json().get("success"))
        self.assertEqual(code, delete_modify.json().get("code"))
        self.assertIn(message, delete_modify.json().get("message"))
