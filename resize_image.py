import cv2
from os import walk, getcwd, path

imgpath_to_imput = r'E:\Images\001'
save_resize_images = r'E:\Images\002'

img_name_list = []
for (dirpath, dirnames, filenames) in walk(imgpath_to_imput):
    img_name_list.extend(filenames)
    break
print(img_name_list)

cnt = 0
for img_name in img_name_list:
    
	img_path = path.join(imgpath_to_imput, img_name)
	img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
	height, width = img.shape[:2]
	print(height)
	print(width)

	if height>400 and width>600:

		print('Original Dimensions : ',img.shape)
		 
		#scale_percent = 60 # percent of original size
		#width1 = int(img.shape[1] * scale_percent / 100)
		#height1 = int(img.shape[0] * scale_percent / 100)
		height = 400
		width = 600
		dim = (width, height)
		print(dim)
		# resize image
		resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
			 
		print('Resized Dimensions : ',resized.shape)
		cv2.imwrite(('%s/%s.JPG'%(save_resize_images,path.splitext(img_name)[0])),resized)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		cv2.imwrite(('%s/%s.JPG'%(save_resize_images,path.splitext(img_name)[0])),img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()