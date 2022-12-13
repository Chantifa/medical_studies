import json

import pprint
from urllib.request import urlopen

import classification_automation
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
param = str("bleeding and lower abdomen pain").replace(" ","%20")
host = "localhost"
port = "8983"
collection = "med_studies"
qt = "select"
defType = "lucene"
facet_sort ="count"
facet="true"
indent="true"
facet_sort="count"
indent="true"
q_op="OR"
q="brief_title"
rows = "10"
wt="json"
url_1 = "http://localhost:8983/solr/med_studies/select?defType=lucene&indent=true&q.op=OR&q=brief_title%3Abreast%20cancer&wt=json"
url_bc = "http://localhost:8983/solr/med_studies/select?defType=lucene&fl=id%2C%20brief_title&fq=gender%3Afemale&indent=true&q.op=OR&q=textblock%3Abreast%20cancer&wt=json"
url = 'http://' + host + ':' + port + '/solr/' + collection + '/' + qt + '?defType='+defType+'&indent='+indent+'&q.op='+q_op+'&q='+q+'%3'+ stop_words.removeStopWord(param)+'&wt='+wt
connection = urlopen(url_bc)
response = json.load(connection)
print(response)

print("Number of hits: " + str(response['response']['numFound']))
pprint.pprint(response['response']['docs'])

ranking_list = []
with open(f'query.json', 'w') as f:
    json.dump(response, f)

def search_param(response):
    with open(f'signal_lung_cancer.json','r') as f:
        data_signal_lc = json.load(f)
    with open(f'signal_breast_cancer.json','r') as f:
        data_signal_bc = json.load(f)
    with open(f'signal_ovarian_cancer.json','r') as f:
        data_signal_oc = json.load(f)
    with open(f'signal_prostate_cancer.json','r') as f:
        data_signal_pc = json.load(f)
    count = 0
    for i in response['response']['docs']:
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
            if id == x:
                ranking_list.append(i)
                print("match in signal prostate cancer",id)
        for x in signal_boosting.prostate_cancer_id:
            if id == x:
                ranking_list.append(i)
                print("match in signal ovarian cancer",id)

        ranking_list.append(i)
        print(ranking_list)
search_param(response)