from PIL import Image
from pytesseract import pytesseract

#generate of thicer file
filenameIn = "bm.bmp"
filenameOut = "out.bmp"
height = 1021
width = 1461

with Image.open(filenameIn) as blank:
    blank.load()
with Image.open(filenameOut) as thicc:
    thicc.load()

for x in range(width):
    for y in range(height):
        if blank.getpixel((x, y)) != 255:
            if x - 1 >= 0:
                thicc.putpixel((x - 1, y), 0)
            if y - 1 >= 0:
                thicc.putpixel((x, y - 1), 0)
            if x + 1 <= width:
                thicc.putpixel((x + 1, y), 0)
            if y + 1 <= height:
                thicc.putpixel((x, y + 1), 0)

thicc.save(filenameOut)
thicc.show()

#erase blank data
filenameDoc = "newtest.jpg"

with Image.open(filenameDoc) as doc:
    doc.load()

widthNew, heightNew = doc.size
if int(heightNew*width/widthNew) < height:
    newSize = height
else:
    newSize = int(heightNew*width/widthNew)
doc.resize((width, newSize))

for x in range(width):
    for y in range(height):
        if thicc.getpixel((x, y)) != 255:
            doc.putpixel((x, y), (255, 255, 255))

#doc.save(filenameDoc)
doc.show()

#read text from image
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(doc, lang='rus')
print(text[:-1])