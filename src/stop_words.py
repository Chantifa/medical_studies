import json

import pandas as pd
import requests

def removeStopWord(query):
    SOLR_URL = 'http://localhost:8983/solr/med_studies/admin/file?wt=json&_=1670963636349&file=lang%2Fstopwords_en.txt&contentType=text%2Fplain%3Bcharset%3Dutf-8'
    res = requests.get(SOLR_URL).text
    stop_words = open('stop_words.txt', 'w')
    stop_words.writelines(res)
    stop_words.close()
    # Using readlines()
    stop_words = open('stop_words.txt', 'r')
    Lines = stop_words.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        stop_word = " "+line.strip()+ " "
        if str(query).__contains__(stop_word):
            query = str(query.lower()).replace(stop_word," ")
    print(query)
    return query

removeStopWord("breast and cancer")