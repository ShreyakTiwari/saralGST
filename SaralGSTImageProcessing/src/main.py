import configparser
import resize
import sys
from flask import request


if __name__ == '__main__':
    config = configparser.ConfigParser()
    #configFilePath = r'/home/shreyak/projects/SaralGSTImageProcessing/config/config.ini'
    configFilePath = sys.argv[1]
    print(configFilePath)
    config.read(configFilePath)
    print(config)
    print(config['DEFAULT']['output_height'])
    obj = resize.Resize(config)
    #obj.resize_simple()
    new_list = obj.return_img()
    print("new_list",new_list)
    for i in new_list:
        obj.resize_image(i)