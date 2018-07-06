import os
import random

#trainval_percent = 0.66
train_percent = 0.9
#xmlfilepath = 'Annotations'
#txtsavepath = '\main'
#imgfilepath = 'image'
imgfilepath = 'JPEGImages'
total_img = os.listdir(imgfilepath)
print (total_img[1:4])
num=len(total_img)
print (num)
list=range(num)
#tv=int(num*trainval_percent)
tr=int(num*train_percent)
#trainval= random.sample(list,tv)
train=random.sample(list,tr)

ftest = open('test.txt', 'w')
ftrain = open('train.txt', 'w')

for i  in list:
    name=total_img[i][:-4]+'\n'
    if i in train:
        ftrain.write(name)
    else:
        ftest.write(name)

ftrain.close()
ftest .close()
