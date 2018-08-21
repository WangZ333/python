#导入Image类
from PIL import Image
image_name = '22.jpg'
img = Image.open(image_name)
img = img.convert('L')
img.save('222.jpg','jpeg')
w,h = img.size
#如果图片太大，将高和宽做一个比例缩放
if w > 100:
	h = int((100/w) * h/2)
	w = 100
	img = img.resize((w,h), Image.ANTIALIAS)
img.save('2222.jpg','jpeg')

#颜色值转换为字符并放到列表
#保存像素字符的列表
data = []
#根据图片宽度和高度遍历像素点并取出每个像素点的颜色
chars = [' ', ',', '1', '+', 'n', 'D', '@', 'M']
for i in range(0, h):
	line = ''
	for j in range(0, w):
		pi = img.getpixel((j,i))
		for k in range(0, 8):
			if pi < (k+1) * 32:
				line += chars[7-k]
				break
	data.append(line)
f = open(image_name+'.txt', 'w')
for d in data:
	print(d, file=f)
f.close()
print('ok!')