# 封装部门管理的添加,查询,修改, 删除
# 导包
import requests


# 定义封装员工类
class DepartmentApi:
    def __init__(self):
        # 定义部门模块的URL
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    def add_dep(self, name, code, headers):
        # 根据外部传入的name和code拼接成要发送的请求体数据
        jsonData = {
            "name": name,
            "code": code,
            "manager": "李某某",
            "introduce": "还是啥",
            "pid": "0000000"
        }
        # 发送添加部门请求，并返回结果
        return requests.post(url=self.dep_url, json=jsonData, headers=headers)

    # 定义查询员工的方法
    def select_dep(self, dep_id, headers):
        # 拼接查询员工的url
        select_url = self.dep_url + "/" + dep_id
        # 发送查询员工的接口请求,并且返回
        return requests.get(url=select_url, headers=headers)

    # 定义修改员工的方法
    def modify_dep(self, json, dep_id, headers):
        # 拼接修改员工的url
        modify_url = self.dep_url + "/" + dep_id
        # 发送修改员工的接口请求,并且返回
        return requests.put(url=modify_url, json=json, headers=headers)

    # 定义删除员工的方法
    def delete_emp(self, emp_id, headers):
        #  拼接删除员工的url
        delete_url = self.dep_url + "/" + emp_id
        # 发送修改员工的接口请求,并且返回
        return requests.delete(url=delete_url, headers=headers)


# 封装hirm登录接口
class LoginApi:
    def __init__(self):
        # 初始化登录的url
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    # 定义获取hirm登录接口的方法
    def login(self, json, headers):
        # 发送登录接口的请求
        return requests.post(url=self.login_url, json=json, headers=headers)