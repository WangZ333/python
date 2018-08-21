#导入Image类
from PIL import Image
image_name = '22.jpg'
img = Image.open(image_name)
img = img.convert('L')
w,h = img.size
img.save('222.jpg','jepg')		