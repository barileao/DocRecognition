import pytesseract as tess
from PIL import Image

imagem=Image.open("pdf2Image/2.jpg")
texto=tess.image_to_string(imagem)

print(texto)