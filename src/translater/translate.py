from deep_translator import GoogleTranslator

def translate(text):
    return GoogleTranslator(source='en', target='es').translate(text)

if __name__ == '__main__':
    print(translate('Hello, world!'))