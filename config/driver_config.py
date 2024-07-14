from selenium import webdriver

class DriverConfig:
    def driver_config(self):

        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')
        # 设置窗口大小
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 去掉“Chrome正受到自动测试软件的控制”
        options.add_argument('--ignore-certificate-errors')
        # 解决selenium无法访问https的问题
        options.add_argument('--allow-insecure-localhost')
        # 允许忽略localhost上的TLS/SSL错误
        # options.add_argument('--incognito')
        # 设置为无痕模式
        # options.add_argument('--headless')
        # 设置为无头模式（不打开浏览器）
        # options.add_argument('--disable-gpu')
        # 解决卡顿(禁用页面GPU)
        # options.add_argument('--no-sandbox')
        # 禁用沙箱

        driver = webdriver.Chrome(executable_path='../driver_files/chromedriver.exe',
                                  options=options)
        driver.delete_all_cookies()
        # 刪除所有cookies

        return driver






