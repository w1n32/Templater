import sys
import configparser


def load_config(file):
    print("Loading variables from config...\n")
    conf = configparser.ConfigParser()
    conf.read(file)
    config_dict = {}
    for section in conf.sections():
        print("Found section:", section)
        items_dict = {}
        for item in conf[section]:
            print("Found item:", item, conf[section][item])
            items_dict.update({item:conf[section][item]})
        config_dict.update({section: items_dict})
    return config_dict


if __name__ == '__main__':
    print(load_config(sys.argv[1]))