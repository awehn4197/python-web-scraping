import wikipedia
from wikipedia import BeautifulSoup ; summary

def wiki_search(topic):
    try:
        return wikipedia.summary(topic, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=2)

#Try typing -  RickRoll
topic = input('What would you like to learn about? ')

print(wiki_search(topic))