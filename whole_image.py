# coding = utf-8
#import cv2
import PIL.Image
import os

def convert(dir,width,height):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        im = PIL.Image.open(path)
        out = im.resize((width,height),PIL.Image.ANTIALIAS)
        print ("%s has been resized!"%filename)
        out.save(path)

if __name__ == '__main__':
   dir = input('please input the operate dir:')
   convert(dir,320,200)
