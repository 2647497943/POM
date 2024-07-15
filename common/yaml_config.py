# with open('../config/environment.yaml', encoding='utf-8') as f:
#     file = f.read()
#     print(file)

import yaml
class GetConf():
    def __init__(self):
        with open('../config/environment.yaml', encoding='utf-8') as file:
            self.env = yaml.load(file, yaml.FullLoader)

    def get_username_password(self):
        return self.env['username'], self.env['password']

    def get_url(self):
        return self.env['url']

if __name__ == '__main__':
    print(GetConf().get_url())

