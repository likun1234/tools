# -*- coding:utf-8 -*-

import os

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
                    if item1.endswith('img.png'):
                        src = os.path.join(os.path.abspath(img_path),item1)
                        dst = os.path.join(os.path.abspath(img_path),  'rgb_' + str(i) + '.jpg')
                        #print(dst)
                #src = os.path.join(os.path.abspath(filelist_1), img_dir)
                #src = os.path.join(os.path.abspath(img_path), item)
                #dst = os.path.join(os.path.abspath(self.path),  + '.jpg')
                #dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')
                        os.rename(src, dst)
                        #print ('converting %s to %s ...' % (src, dst))
                i = i + 1

        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
