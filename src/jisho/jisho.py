import requests
from bs4 import BeautifulSoup
from translater import translate

def get_jisho_data(word):
    data = requests.get(f"https://jisho.org/search/{word}").text
    soup = BeautifulSoup(data, "html.parser")
    for response in soup.find("span", {"class": "meaning-meaning"}):
        return(word, response.text)
    return(word, "No definition found")


def jisho_traduction(word):
    data = get_jisho_data(word)
    translated_data = translate.translate(data[1])
    return word, translated_data
    
if __name__ == "__main__":
    a = get_jisho_data("くろ")
    print(a)