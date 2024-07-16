from time import sleep

from POM.config.driver_config import DriverConfig
from POM.page.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'admin')
        # driver.get('http://192.168.2.203:8080/jpress/user/login')
        # LoginPage().login_input_value(driver, "请输入账号或邮箱", 'zzz')
        # LoginPage().login_input_value(driver, '及密码...', '123')
        # LoginPage().click_login(driver, ' 登 录 ')
        sleep(10)
        # driver.quit()
