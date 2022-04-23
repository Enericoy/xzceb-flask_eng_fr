import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#text_to_translate='Hello, how are you today?'
TEXT="Bonjour, comment vous êtes aujourd'hui?"

#check language
language = language_translator.identify(
    TEXT).get_result()
#print(json.dumps(language, indent=2))

detected_language=language['languages'][0]['language']
#print(detected_language)

def english_to_french(englishText):
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText=translation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText

if detected_language=="fr" :
    #print('The language is French')
    english_Text=french_to_english(TEXT)
    #print("French Text : ", TEXT)
    #print("English Text : ", english_Text)
elif detected_language=="en":
    #print('The language is English')
    french_Text=english_to_french(TEXT)
    #print("English Text : ", TEXT)
    #print("French Text : ", french_Text)
