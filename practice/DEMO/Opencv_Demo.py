#在开头引入必要的库
import matplotlib.pyplot as plt
import numpy as np
import cv2


#读取一张图片


lenna_img = cv2.imread("E:\zhou.jpg")
#opencv默认的imread是以BGR的方式进行存储的,
# 而matplotlib的imshow默认则是以RGB格式展示,所以此处我们必须对图片的通道进行转换
lenna_img2 = cv2.cvtColor(lenna_img,cv2.COLOR_BGR2RGB)

cv2.imwrite('E:\cope_lenna_img.jpg',lenna_img)#注意通道模式不一样

plt.imshow(lenna_img2)
plt.axis("off")
plt.show()