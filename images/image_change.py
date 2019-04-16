from PIL import Image

img_file = 'background.jpg'
new_size = (5000, 3000)
new_name = "new_{}".format(img_file)

Image.open(img_file).resize(new_size, Image.ANTIALIAS).save(new_name)
