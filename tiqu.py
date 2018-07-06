# -*- coding:utf-8 -*-

import os
import cv2
import numpy as np
import shutil
class ImageRename():
    def __init__(self):
        self.path = '/media/lk/Seagate Backup Plus Drive/总结_DL/data/test_mask_10'

    def rename(self):
        filelist = os.listdir(self.path)
        #print(filelist)
        total_num = len(filelist)

        i = 0

        for item in filelist:
            if item.endswith('_json'):
                print(item)
                img_path = os.path.join(os.path.abspath(self.path),item)
                filelist_1 = os.listdir(img_path)
                print(filelist_1)
                for item1 in filelist_1:
                    if item1.startswith('img'):
                        print(item1)
                        src = os.path.join(os.path.abspath(img_path),item1)
                        image = cv2.imread(src)
                        dst = os.path.join(os.path.abspath(self.path), 'rgb', 'rgb_' + str(i) + '.jpg')
                        print(dst)
                        cv2.imwrite(dst, image)
                        #shutil.copyfile(src,dst)
                        #os.rename(src, dst)
                        #print ('converting %s to %s ...' % (src, dst))
                i = i + 1

        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
