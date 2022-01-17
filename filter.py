from PIL import Image, ImageFilter

#you can place your own picture in palce of photo.jpg and it can be of any extension
before  = Image.open("photo.jpg")

#you can use any filter from the ImageFilter function..(you can select from the list)
after = before.filter(ImageFilter.EDGE_ENHANCE)

#you can give the output repository your own name and the output file can be of other extension
after.save("out.bmp")
