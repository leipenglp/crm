import yaml
# with open('test.yaml') as yaml_file:
#     data=yaml.load(yaml_file,yaml.FullLoader)
# print(data['LoginPage']['password'])
class YamlOperation:
    def __init__(self,locator_file):
        with open(locator_file) as yaml_file:
            self.data = yaml.load(yaml_file, yaml.FullLoader)
    def get_locator(self,page,local):
        return self.data[page][local]
