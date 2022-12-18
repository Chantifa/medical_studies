import json
from urllib.request import urlopen

import signal_boosting
import stop_words

"""
Query parameter for json to Solr
"q": "textblock: {breast cancer}",
"defType": "lucene",
"indent": "true",
"fl": "id, brief_title",
"q.op": "OR",
"fq": "gender:female",
"wt": "json",
"_": "1670920539814

"""


def search_param(query):
    param = stop_words.removeStopWord(query)
    param = str(param).replace(" ", "%20")
    host = "localhost"
    port = "8983"
    collection = "med_studies"
    qt = "select"
    defType = "lucene"
    facet_sort = "count"
    facet = "true"
    indent = "true"
    facet_sort = "count"
    indent = "true"
    q_op = "OR"
    q = "brief_title"
    rows = "10"
    wt = "json"
    url = 'http://' + host + ':' + port + '/solr/' + collection + '/' + qt + '?defType=' + defType + '&indent=' + indent + '&q.op=' + q_op + '&q=' + q + '%3A' + param + '&wt=' + wt
    print(url)
    connection = urlopen(url)
    res = json.load(connection)
    ranking_list = []
    count = 0
    for i in res['response']['docs']:
        print("Number of hits: " + str(res['response']['numFound']))
        count += 1
        id = i['id']
        for x in signal_boosting.lung_cancer_id:
            if id == x:
                ranking_list.append(i)
                print("match in signal lung cancer",id)
        for x in signal_boosting.breast_cancer_id:
            if id == x:
                ranking_list.append(i)
                print("match in signal breast cancer",id)
        for x in signal_boosting.ovarian_cancer_id:
            if id == x:
                ranking_list.append(i)
                print("match in signal prostate cancer",id)
        for x in signal_boosting.prostate_cancer_id:
            if id == x:
                ranking_list.append(i)
                print("match in signal ovarian cancer",id)
        with open(f'query.json', 'w') as f:
            json.dump(res, f)
    connection2 = urlopen(url)
    res2 = json.load(connection2)
    for n in res2['response']['docs']:
        ranking_list.append(n['id'])
    ranking_list.reverse()
    print(ranking_list)
    print("Number of hits: " + str(res['response']['numFound']))
search = "lung and cancer"
search_param(search)
