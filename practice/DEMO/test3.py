from PIL import Image

 #  load a color image 
image_name = 'WZ.jpg'

im  =  Image.open( image_name)

 #  convert to grey level image 
Lim  =  im.convert( 'L' )
Lim.save( 'wangzhengl.jpg' )

# Pim  =  im.convert( 'P' )
# Pim.save( 'wangzheng4.jpg' )
 #  setup a converting table with constant threshold 
threshold1 =  80
threshold = 40
table  =  []
for  i  in  range( 256 ):
     if  i  <  threshold1:
     	if i < threshold:
     		table.append(0)
     	else :
     		table.append(1)
     else :
         table.append(1)

 #  convert to binary image by the table 
bim  =  Lim.point(table,  '1' )

bim.save( 'wangzheng2.jpg' ) 
print('ok!')