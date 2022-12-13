import requests

def removeStopWord(query):
    SOLR_URL = 'http://localhost:8983/solr/med_studies/admin/file?wt=json&_=1670963636349&file=lang%2Fstopwords_en.txt&contentType=text%2Fplain%3Bcharset%3Dutf-8'
    response = requests.get(SOLR_URL).text
    list_of_terms = response
    ## Create list of tuples
    tuple_list = []
    for i in range(len(list_of_terms)):
        if list_of_terms[i].__contains__('#'):
            print("")
        else:
             tuple_list.append(list_of_terms[i])
            # Filter out all irrelevant list
    for x in tuple_list:
        if str(query).__contains__(x):
            new_query = str(query).replace(x," ")
    return new_query