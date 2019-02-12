import sys
import os
import configparser
from jinja2 import Environment, FileSystemLoader


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


def render_template(dir_name, file_name, variables_dict):
    print("Render template...")
    file_loader = FileSystemLoader(dir_name)
    env = Environment(loader=file_loader)
    template = env.get_template(file_name)
    return template.render(tv=variables_dict)


if __name__ == '__main__':
    template_vars = load_config(sys.argv[1])
    dirs = os.listdir(path='.')
    for item in template_vars:
        if item in dirs:
            print("Processing in directory:", item)
            for file in os.listdir(item):
                print(render_template(item, file, template_vars[item]))