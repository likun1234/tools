import os
#import random
#import cv2
import shutil
imgfile = os.listdir('/home/lk/deep_learning/FCN-2018-5-09/image')
imgfile.sort(key=lambda x:int(x[:-4]))#按照序号大小来排序
len_file = len(imgfile)
#Mat img
print (imgfile)
ii = 0
for i in imgfile:

    #img = cv.imread(imgfile[i],1)
    aa,bb = i.split(".")
    if ii<10:
        img_new_file = '00{}'.format(ii)
    elif ii>=10 or ii<100:
        img_new_file = '0{}'.format(ii)
    elif ii>=100:
        img_new_file = '{}'.format(ii)
    else:
        print("num excess!")
    ii = ii + 1
    newname = '/home/lk/deep_learning/FCN-2018-5-09/oo/' + img_new_file
    os.mkdir(newname)
    oldname = '/home/lk/deep_learning/FCN-2018-5-09/image/' + aa + '.' + bb
    newname = newname + '/' + aa + '.' + bb
    shutil.copyfile(oldname,newname)
