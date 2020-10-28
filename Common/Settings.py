import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

text = config['Text']