
from wand.image import Image as Img
import time

pegarPDF = input("Insira o nome do PDF ")
with Img(filename=pegarPDF, resolution=300) as img:
   pegarponto = pegarPDF.strip(".pdf")
   pegarponto = pegarponto + ".jpg"	
   img.compression_quality = 99
   img.save(filename=pegarponto)



# img = Image.open ('image_name.jpg') 
# crop_img = img.crop ((x1, y1, x2, y2)) 
# crop_img.save ('amount.jpg')

import pytesseract
# import numpy
# import cv2

from PIL import Image



# image = Image.open(pegarponto).convert('RGB')


# npimagem = np.asarray(imagem).astype(np.uint8)  

# npimagem[:,:, 0] = 0
# npimagem[:,:, 2] = 0

# im = cv2.cvtColor(npimagem, cv2.COLO_RGB2GRAY)
start = time.time()

text = pytesseract.image_to_string(Image.open(pegarponto))
print(text)


end = time.time()
print(end - start)

# img = cv2.imread(pegarponto,0)
# edges = cv2.Canny(img,100,200)
# img_new = Image.fromarray(edges)
# text = pytesseract.image_to_string(img_new, lang='por')
# print (text)
