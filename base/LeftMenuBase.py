class LeftMenuBase():
    def level_one_menu(self, menu_name):
        return "//aside[@class='main-sidebar']//span[text()='" + menu_name + "']"

    def level_two_menu(self, menu_name):
        return "//aside[@class='main-sidebar']//a[text()='" + menu_name + "']"


if __name__ == '__main__':
    print(LeftMenuBase().level_two_menu("评论"))
