import requests

API_URL = "https://voxa-translate.replit.app/api"

class Translator:
    def __init__(self, source='en', target='fr'):
        self.source = source
        self.target = target

    def translate(self, text, target=None):
        target_language = target if target else self.target

        response = requests.get(API_URL, params={
            'translate': text,
            'from': self.source,
            'to': target_language
        })

        data = response.json()
        return data.get("translated", "")