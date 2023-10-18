import configparser

config = configparser.RawConfigParser()
file = "C:\\Users\\Raj\\PycharmProjects\\Cermati\\Configuration\\config.ini"
config.read(file)


class Read_Config:
    @staticmethod
    def read_url():
        Url = config.get('common data', 'url')
        return Url

    @staticmethod
    def read_username():
        Username = config.get('common data', 'usename')
        return Username

    @staticmethod
    def read_password():
        Password = config.get('common data', 'url')
        return Password
