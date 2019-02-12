import sys
import configparser


def LoadConfig(ConfigFile):
    conf = configparser.ConfigParser()
    try:
        conf.read(ConfigFile)
    except Exception as err:
        sys.stdout("We have a problem")
        sys.stdout(err)