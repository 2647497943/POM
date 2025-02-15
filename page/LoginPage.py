from time import sleep

from selenium.webdriver.common.by import By

from POM.base.LoginBase import LoginBase
from POM.base.ObjectMap import ObjectMap

from POM.common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页面输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_btn(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        """
        登录
        :param driver:
        :param user:
        :return:
        """
        self.element_to_url(driver, "/jpress/admin/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, '请输入账号或邮箱', username)
        self.login_input_value(driver, '及密码...', password)
        sleep(5)
        self.click_login(driver, ' 登 录 ')
        # driver.find_element_by_xpath("//button[@type='submit']").click()
