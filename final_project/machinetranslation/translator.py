"""
Module for the running the translator Functions.
Imported: json, os, LanguageTranslatorV3 from ibm_watson,
IAMAuthenticator from ibm_cloud_sdk_core.authenticators,
load_dotenv from dotenv
Purpose is to compare expected outputs to function outputs.
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version='2022-07-11', authenticator=authenticator)
language_translator.set_service_url(URL)
ENGLISH_TEXT = 'I am'
FRENCH_TEXT = 'Je suis'
def english_to_french(english_txt):
    'Convert English string to French'
    processing = language_translator.translate(text=english_txt, model_id = 'en-fr').get_result()
    french_text = processing['translations'][0]['translation']
    return french_text
def french_to_english(french_txt):
    'Convert French string to English'
    processing = language_translator.translate(text=french_txt, model_id = 'fr-en').get_result()
    english_text = processing['translations'][0]['translation']
    return english_text
english_to_french(ENGLISH_TEXT)
french_to_english(FRENCH_TEXT)
