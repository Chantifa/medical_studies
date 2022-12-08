import requests

SOLR_URL = 'http://localhost:8983/solr/med_studies/admin/file?wt=json&_=1670150313749&file=lang%2Fstopwords_en.txt&contentType=text%2Fplain%3Bcharset%3Dutf-8'
response = requests.get(SOLR_URL)
list_of_terms = response.json()['terms']['_text_']
## Create list of tuples
tuple_list = []
for i in range(len(list_of_terms)):
    if i % 2 == 1:
        tuple_list.append((list_of_terms[i-1],list_of_terms[i]))
# Filter out all irrelevant list
filterd_list = [t for t in tuple_list if t[1] != 1]
filterd_list