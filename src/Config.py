# -*- coding: utf-8 -*-
# https://docs.python.org/ja/3/library/configparser.html#interpolation-of-values
from configparser import ConfigParser, ExtendedInterpolation
CONFIG_INI_PATH = './Config.ini'

def gen_parser():
    return ConfigParser(interpolation=ExtendedInterpolation())

def read():
    config = gen_parser()
    config.read(CONFIG_INI_PATH)
    return config

def reader(config, search_keys):
    data = None # search_keys で config を下るたびに更新される
    for k in search_keys :
        if data != None and k in data:
            data = data[k]
        elif k in config:
            data = config[k]

    return data


if __name__ == '__main__':
    import sys

    # Config.ini の中身を読む
    config = read()

    # ./Config.ini Example:
    # ```
    # [Paths]
    # datad = ./data
    # ```
    #
    # $ python3 /path/to/Config.py "Paths" "datad"
    # ./data # <- 改行なしで印字
    print(reader(config, sys.argv[1:]), end='')

