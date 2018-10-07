import pytesseract
import time

from wand.image import Image as Img
from PIL import Image


pegarPDF = input("Insira o nome do PDF ")
with Img(filename=pegarPDF, resolution=300) as img:
   pegarponto = pegarPDF.strip(".pdf")
   pegarponto = pegarponto + ".jpg"

   img.compression_quality = 99

   img.save(filename=pegarponto)

start = time.time()

text = pytesseract.image_to_string(Image.open(pegarponto))
print(text)


end = time.time()
print(end - start)
