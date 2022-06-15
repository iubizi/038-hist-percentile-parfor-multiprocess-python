import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('119_4.JPG')
img = np.array(img, dtype='int')
print(img.shape)

gray = img[:,:,0] + img[:,:,1] + img[:,:,2]
'''
print(gray.shape)
print(np.max(gray))
print(np.min(gray))
'''

plt.imshow(gray)
# plt.show()



white = np.percentile(gray, 99)
mask = gray>=white # 只需要最亮的1%，之后做白平衡
print(mask)

r = np.mean(img[mask, 0])
g = np.mean(img[mask, 1])
b = np.mean(img[mask, 2])
print(r,g,b)

plt.imshow(mask, alpha=0.8)
plt.show()


'''
# 会显示一大堆，因为是二维，所以每一行都会做直方图
plt.hist( gray, bins=10,
          facecolor='blue', edgecolor='black',
          alpha=0.7 )
plt.show()
'''
