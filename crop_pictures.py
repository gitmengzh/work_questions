# 裁剪图片

import os
from PIL import Image
p_path = os.path.abspath('..')
img_path = os.path.dirname(p_path)+'/test_file/'
ext = ['jpg', 'jpeg', 'png']
files = os.listdir(img_path)


def process_image(filename, mwidth=200, mheight=400):
    image = Image.open(filename)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(filename, 'is OK.')
        return
    if (1.0 * w / mwidth) > (1.0 * h / mheight):
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    new_im.save(filename)
    new_im.close()


for file in files:
    if file.split('.')[-1] in ext:
        process_image(img_path+file)