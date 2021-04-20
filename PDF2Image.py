#pip install pdf2image
import os
from pdf2image import convert_from_path

outputFolder = "pdf2Image/"

def convert(file, outputFolder):
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    pages = convert_from_path(file,500)
    counter = 1

    for page in pages:
        myFile = outputFolder + str(counter) + '.jpg'
        counter = counter+1
        page.save(myFile)


file = "C:\\Users\\mariana.leao\\Downloads\\acument_20210407_1453.pdf"
convert(file, outputFolder)
