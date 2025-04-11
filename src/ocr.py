from imports import *

def image_to_text(imagepath):
    imagepath = imagepath
    return tess.image_to_string(imagepath,lang='deu')


print(tess.get_languages(config=''))
test_text = image_to_text("testimages/german2.jpeg")

# idea: image comes in, OCR is done
# lang is detected after 






