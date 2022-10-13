"""EN/FR TRANSLATOR"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = 'eJtvW_30PvuAViGxW1aa5ruP5aCX0cvlv77h0biLOyFg'
URL = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6cbc080e-b535-4e73-9506-8e90fc762eea'

# Prepare the Authenticator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def e2f(text_to_translate):
    """Takes English, returns French"""
    translation = language_translator.translate(
        text = text_to_translate,
        model_id='en-fr').get_result()
    return translation

def f2e(text_to_translate):
    """Takes French, returns English"""
    translation = language_translator.translate(
        text = text_to_translate,
        model_id='fr-en').get_result()
    return translation

