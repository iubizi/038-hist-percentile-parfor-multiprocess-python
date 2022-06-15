import matplotlib.image as mpimg
import numpy as np
import os

import gc
gc.enable()

fw = open('left.csv', 'w')
print('name,r,g,b', file=fw)
fw.close()

path = 'Left_Irises/Eye-Pictures/'
files = os.listdir(path)

####################
# 处理一张
####################

def process(file):

    img = mpimg.imread( path + file ) # 遍历文件
    img = np.array(img, dtype='int')
    gray = img[:,:,0] + img[:,:,1] + img[:,:,2]

    white = np.percentile(gray, 99) # 筛选出来的白色区域

    r = np.mean(img[gray>white, 0])
    g = np.mean(img[gray>white, 1])
    b = np.mean(img[gray>white, 2])

    fw = open('left.csv', 'a') # 非同步状态下这么做可以不用写同步，简单高效

    print(file, file=fw, end=',') # 立刻写入
    # print(file)
    
    print(r, file=fw, end=',')
    print(g, file=fw, end=',')
    print(b, file=fw)

    fw.close()

####################
# 多进程
####################

from multiprocessing import Pool

if __name__ == '__main__':
    
    pool = Pool() # python来决定 processes=16/24/32 没区别，python不会用爆cache
    pool.map(process, files)
    pool.close()
    pool.join()
