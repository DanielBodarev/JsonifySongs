import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

song = config['Song']
songbook = config['Songbook']
misc = config['Misc']