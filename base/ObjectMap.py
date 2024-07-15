import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException

from POM.common.yaml_config import GetConf


class ObjectMap():
    url = GetConf.get_url()
    # 获取基础地址

    def element_get(self, driver, loc_type, loc_value, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver:浏览器驱动
        :param loc_type:定位方式类型
        :param loc_value:定位表达式
        :param timeout:超时时间
        :param must_be_visible:元素是否必须可见，True是必须可见 False是默认值
        :return:返回的元素
        """
        start_time = time.time() * 1000
        # 开始时间
        stop_ms = start_time + (timeout * 1000)
        # 结束时间
        for i in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=loc_type, value=loc_value)
                if not must_be_visible:
                    # 如果元素不是必须可见，就直接返回元素
                    return element
                else:
                    # 如果元素必须是可见的，则需要先判断元素是否可见
                    if element.is_displayed():
                        return
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式： " + loc_type + " 定位表达式： " + loc_value)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        start_ms = time.time() * 1000
        # 开始时间
        stop_ms = start_ms + timeout * 1000
        # 结束时间
        for i in range(int(timeout * 10)):
            try:
                ready_state = driver.excute_script("return document.readyState")
            except WebDriverException:
                time.sleep(0.03)
                # 如果有driver的错误，执行js会失败，就直接跳过
                return True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    # 如果超时了就break
                    break
                time.sleep(0.1)
        raise Exception(f"打开网页时，页面元素在{timeout}秒后仍然没有完全加载完")

    def element_disappear(self, driver, loc_type, loc_value, timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器
        :param loc_type: 定位方式
        :param loc_value: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        start_ms = time.time() * 1000
        # 开始时间
        stop_ms = start_ms + timeout * 1000
        # 结束时间
        if loc_type:
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=loc_type, value=loc_value)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式： " + loc_type + "定位表达式：" + loc_value)
        else:
            pass

    def element_appear(self, driver, loc_type, loc_values, timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param loc_type:
        :param loc_values:
        :param timeout:
        :return:
        """
        if loc_type:
            start_ms = time.time() * 1000
            # 开始时间
            stop_ms = start_ms + timeout * 1000
            # 结束时间
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=loc_type, value=loc_values)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
                raise ElementNotVisibleException("元素没有出现，定位方式：" + loc_type + " 定位表达式：" + loc_values)
        else:
            pass
    def element_to_url(
            self,
            driver,
            url,
            loc_type_disappear=None,
            loc_value_disappear=None,
            loc_type_appear=None,
            loc_value_appear=None
    ):
        """
        跳转地址
        :param driver:浏览器驱动
        :param url: 地址
        :param loc_type_disappear:等待页面元素消失的定位方式
        :param loc_value_disappear:等待页面元素消失的定位表达式
        :param loc_type_appear:等待页面元素出现的定位方式
        :param loc_value_appear:等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.url+url)

            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待元素消失
            self.element_disappear(
                driver,
                loc_type_disappear,
                loc_value_disappear
            )
            # 跳转后等待元素出现
            self.element_appear(
                driver,
                loc_type_appear,
                loc_value_appear
            )
        except Exception as e:
            print(f'跳转地址出现异常，异常原因：{e}')
