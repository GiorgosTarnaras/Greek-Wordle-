import random
import urllib.request
from bs4 import BeautifulSoup
url = "https://sites.google.com/site/dimizaro/lexiko/lexeis5grammaton"

def get_word():
    with urllib.request.urlopen(url) as response:
            byte_file = response.read()#αρχείο σε byte που περιέχει το hmtl που πείραμε από τον σύνδεσμο
    my_str = byte_file.decode("utf-8")
    soup = BeautifulSoup(my_str, "html.parser")
    table =  soup.find_all("table")
    words = str(table[-1]).split("\n")
    while True:
        word = random.choice(words)
        if len(word) == 5: break
    return word





