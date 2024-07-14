class LoginBase():
    def login_input(self, input_placeholder):
        return "//input[@placeholder='"+input_placeholder+"']"

    def login_btn(self,button_name):
        return "//button[text()='"+button_name+"']"


if __name__ == '__main__':
    print(LoginBase().login_input('请输入账号或邮箱'))
    print(LoginBase().login_input('及密码...'))
    print(LoginBase().login_btn("登 录"))