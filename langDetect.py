import nltk
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
import json


def languageRatios(text):
    ratios = {}
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        matchingElements = words_set.intersection(stopwords_set)
        ratios[language] = len(matchingElements)
    highestRateLanguage = max(ratios, key=ratios.get)
    l = {"language":""}
    l["language"] = highestRateLanguage
    return l