import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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
text_to_translate="Hola, ¿cómo estás hoy?"

#check language
language = language_translator.identify(
    text_to_translate).get_result()
#print(json.dumps(language, indent=2))

detected_language=language['languages'][0]['language']
#print(detected_language)

if detected_language=="es" :
    print('The language is Spanish')
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='es-en').get_result()
    print("Spanish Text : ", text_to_translate)
    print("English Text : ", translation['translations'][0]['translation'])
elif detected_language=="en":
    print('The language is English')
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='en-es').get_result()
    print("English Text : ", text_to_translate)
    print("Spanish Text : ", translation['translations'][0]['translation'])


#json_response=json.dumps(translation, indent=2, ensure_ascii=False)
#print(json.dumps(translation, indent=2, ensure_ascii=False))
#print(json_response)
