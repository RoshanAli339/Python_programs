from PIL import Image, ImageFilter

before  = Image.open("photo.jpg")
after = before.filter(ImageFilter.EDGE_ENHANCE)
after.save("out.jpg")
