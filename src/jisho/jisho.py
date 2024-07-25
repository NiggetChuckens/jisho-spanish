import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def translate(text):
    return GoogleTranslator(source='en', target='es').translate(text)


def get_jisho_data(word):
    data = requests.get(f"https://jisho.org/search/{word}").text
    soup = BeautifulSoup(data, "html.parser")
    for response in soup.find("span", {"class": "meaning-meaning"}):
        return(word, response.text)
    return(word, "No definition found")


def get_jisho_sentence(word):
    data = requests.get(f"https://jisho.org/search/{word}").text
    soup = BeautifulSoup(data, "html.parser")
    return [response.text for response in soup.find_all("span", {"class": "japanese_word__text_wrapper"})]

def jisho_traduction(word):
    data = get_jisho_data(word)
    translated_data = translate(data[1])
    return word, translated_data
    
if __name__ == "__main__":
    a = get_jisho_sentence("プをして")
    for word in a:
        print(jisho_traduction(word))