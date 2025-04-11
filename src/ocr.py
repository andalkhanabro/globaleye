#! /usr/bin/env python3

from imports import *


SUPPORTED_LANGS = [
    'eng',  
    'fra',  
    'deu', 
    'spa', 
    'ita',  
    'por',  
    'rus',
    'ara', 
    'hin',
    'jpn',  
    'chi_sim',
    'kor', 
    'tur', 
    'heb',  
    'ben',  
    'tam',  
    'urd',  
    'vie',  
]

LANG_STRING = "+".join(SUPPORTED_LANGS)

def image_to_text(imagepath, user_lang=None):
    imagepath = imagepath

    if user_lang is None:
        return tess.image_to_string(imagepath, lang = LANG_STRING) # adding too many langs can confuse extraction...
    else: 
        return tess.image_to_string(imagepath, lang = user_lang) # TODO: probably check if user inputted lang is a supported lang or ALLOW from a supported menu 

test_text = image_to_text("testimages/german2.jpeg")
print(f"Raw Text: {test_text}")