import sys
import os
from PIL import Image
from resizeimage import resizeimage
import configparser
import logging

# use logger
# use config
# use error and exception
class Resize:

    def __init__(self,config):
        self.config = config
        print(config['path']['input_img_path'])
        
    def resize_simple(self):
        with open('/home/shreyak/projects/SaralGSTImageProcessing/data/Kingfisher.jpg','r+b') as f:
            with Image.open(f) as image:
                w, h = 1000, 500
                cover = resizeimage.resize_cover(image, [w, h])
                cover.save('/home/shreyak/projects/SaralGSTImageProcessing/data/sample_ouput.jpg', optimize=True, quality=90 )

    '''
    return list of images in the directory mentioned in the config
    '''
    def return_img(self):
        dir = self.config['path']['input_img_path']
        print(dir)
        img_list = os.listdir(dir)
        print(img_list)
        return img_list

    '''
    resize image with dimensions mentioned in the config
    '''
    def resize_image(self, img_name):
        print("omg_path",img_name)
        img_path = self.config['path']['input_img_path']
        print('type',type(int(self.config['DEFAULT']['output_height'])))
        with open( os.path.join(img_path,img_name), 'r+b') as f:
            with Image.open(f) as image:
                w, h = image.size
                print("Width: ", w)
                print("height: ", h)
                cover = resizeimage.resize_cover(image, [int(self.config['DEFAULT']['output_height']), int(self.config['DEFAULT']['output_width'])])
                Resize.save_img(self, cover, image, img_name)     
        

    '''
    save img 
    input 
    image: image to be saved
    img_name: name of the image 
    '''
    def save_img(self, cover, image, img_name):
        output_path = self.config['path']['output_img_path']
        cover.save(os.path.join(output_path,img_name), image.format, optimize=True, quality=int(self.config['img_properties']['low_quality']))  