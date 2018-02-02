

#  实例化configParser对象
import configparser

config = configparser.ConfigParser()

#  读取config.ini文件
config.read('config.ini')


def getMqValue(name):
    return config.get('rabbitmq', name)

def getDbValue(name):
    return config.get('db', name)