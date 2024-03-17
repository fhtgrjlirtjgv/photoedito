from PIL import Image, ImageFilter


with Image.open("banka.png") as original:
    pic_gray = original.convert("L")
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_gray.save('bw_pic.png')
    pic_blur.save('blur_pic.png')
    pic_gray.show()
