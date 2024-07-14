class AdminBase():
    def wenzhang(self):
        return "//span[text()='文章']"

    def logo_jpress(self):
        return "//span[@class='logo-lg']/b"
        # return "//b[contains(text(), 'Jpress')]"

    def ninhao(self):
        return "//span[starts-with(text(), '您好')]"

print(AdminBase().ninhao())
