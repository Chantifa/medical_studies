import json
import random
from datetime import datetime
from random import randint, choice, shuffle
from urllib.request import urlopen
from faker import Faker
import pandas as pd

connection_bc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Abreast%20cancer&wt=json")
relevantDocument_bc = json.load(connection_bc)


def breast_cancer():
    breast_cancer_array = []

    for i in relevantDocument_bc['response']['docs']:
        query = str(i['brief_title']).lower().replace("\'", "").replace("\'", "").strip()
        condition = str(i['condition']).lower().replace("\'", "").replace("\'", "").strip()
        target = i['id']
        type = random.choice(["click", ""])
        weight = random.randint(1, 4)
        timestamp = datetime.now()
    breast_cancer_array.append(
        str('["query":"{}","timestamp":"{}","condition":"{}","type":"click","weight":"{}","target":"{}"]').format(
            query,
            timestamp,
            condition,
            type,
            weight, target))
    return breast_cancer_array

def breast_cancer_id():
    tuple_relevantDocument_bc = []
    for i in relevantDocument_bc['response']['docs']:
        tuple_relevantDocument_bc.append(i['id'])
        tuple_relevantDocument_bc.sort()
    return tuple_relevantDocument_bc

connection_pc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=prostate%20cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Aprostate%20cancer")
relevantDocument_pc = json.load(connection_pc)

def prostate_cancer():
    prostate_cancer_array = []
    for i in relevantDocument_pc['response']['docs']:
        query = str(i['brief_title']).lower().replace("\'", "").replace("\'", "").strip()
        timestamp = datetime.now()
        condition = str(i['condition']).lower().replace("\'", "").replace("\'", "").strip()
        type = random.choice(["click", ""])
        weight = random.randint(1, 4)
        target = i['id']
    prostate_cancer_array.append(
        str('["query":"{}","timestamp":"{}","condition":"{}","type":"click","weight":"{}","target":"{}"]').format(
            query,
            timestamp,
            condition,
            type,
            weight, target))
    return prostate_cancer_array

def prostate_cancer_id():
    tuple_relevantDocument_pc = []
    for i in relevantDocument_pc['response']['docs']:
        tuple_relevantDocument_pc.append(i['id'])
        tuple_relevantDocument_pc.sort()
    return tuple_relevantDocument_pc

connection_lc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=lung%20cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Alung%20cancer")
relevantDocument_lc = json.load(connection_lc)

def lung_cancer():
    lung_cancer_array = []
    for i in relevantDocument_lc['response']['docs']:
        query = str(i['brief_title']).lower().replace("\'", "").replace("\'", "").strip()
        condition = str(i['condition']).lower().replace("\'", "").replace("\'", "").strip()
        target = i['id']
        type = random.choice(["click", ""])
        weight = random.randint(1, 4)
        timestamp = datetime.now()
    lung_cancer_array.append(
        str('["query":"{}","timestamp":"{}","condition":"{}","type":"click","weight":"{}","target":"{}"]').format(
            query,
            timestamp,
            condition,
            type,
            weight, target))
    return lung_cancer_array

def lung_cancer_id():
    tuple_relevantDocument_lc = []
    for i in relevantDocument_lc['response']['docs']:
        tuple_relevantDocument_lc.append(i['id'])
        tuple_relevantDocument_lc.sort()
    return tuple_relevantDocument_lc

connection_oc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=ovarian%20cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Aovarian%20cancer")
relevantDocument_oc = json.load(connection_oc)

def ovarian_cancer():
    ovarian_cancer_array = []
    for i in relevantDocument_oc['response']['docs']:
        query = str(i['brief_title']).lower().replace("\'", "").replace("\'", "").strip()
        condition = str(i['condition']).lower().replace("\'", "").replace("\'", "").strip()
        type = random.choice(["click", ""])
        target = i['id']
        weight = random.randint(1, 4)
        timestamp = datetime.now()
    ovarian_cancer_array.append(
        str('["query":"{}","timestamp":"{}","condition":"{}","type":"click","weight":"{}","target":"{}"]').format(
            query,
            timestamp,
            condition,
            type,
            weight, target))
    return ovarian_cancer_array


def ovarian_cancer_id():
    tuple_relevantDocument_oc = []
    for i in relevantDocument_oc['response']['docs']:
        tuple_relevantDocument_oc.append(i['id'])
        tuple_relevantDocument_oc.sort()
    return tuple_relevantDocument_oc


breast_cancer = breast_cancer()
breast_cancer_id = breast_cancer_id()

prostate_cancer = prostate_cancer()
prostate_cancer_id = prostate_cancer_id()

lung_cancer = lung_cancer()
lung_cancer_id = lung_cancer_id()

ovarian_cancer = ovarian_cancer()
ovarian_cancer_id = ovarian_cancer_id()

with open(f'signal_breast_cancer.json', 'w') as f:
    json.dump(breast_cancer, f)

with open(f'signal_lung_cancer.json', 'w') as f:
    json.dump(lung_cancer, f)

with open(f'signal_prostate_cancer.json', 'w') as f:
    json.dump(prostate_cancer, f)

with open(f'signal_ovarian_cancer.json', 'w') as f:
    json.dump(ovarian_cancer, f)

queries = [
    {
        'condition': 'lung cancer',
        'relevantDocuments': ['2fa59bcb-e895-4d30-ba7e-4bdbb71d5e6f, 7c274ec5-b9a2-46a7-ac58-6665a0183399',
                              '613e52cd-77e5-472b-aac1-7396a8164a0c', '685c3a36-d87f-4124-aaf8-7510808aedac']
    },
    {
        'condition': 'breast cancer',
        'relevantDocuments': ['22891b87-2036-45f4-b56c-b11335e497c6', '4665289a-3130-4f47-8ead-a33016b8c41e',
                              '1b00d613-62f3-42ab-b0d4-0c916a338282', '0bf57215-acf7-45fb-8a92-2bb6b8162db8',
                              '0bf57215-acf7-45fb-8a92-2bb6b8162db8']
    },
    {
        'condition': 'prostate cancer',
        'relevantDocuments': ['ecab8725-fd5a-43dd-a1c0-375b093d660c', '68db61e5-595a-428f-b5c0-6a1b27c12b4c',
                              '7224cfdf-e0a7-4445-bd72-4b6e4fa4dce4', '193c6698-48c7-4c47-9716-e2e646e11c32',
                              '6042129b-97c7-4984-8195-fe7f592660cd']
    },
    {
        'condition': 'ovarian cancer',
        'relevantDocuments': ['9360ba08-5979-4a2d-aaeb-e3c3f8475a24', 'd097cffd-7244-4494-a86c-4f32bbbf57f5',
                              'c965c937-482c-43a8-a94f-9cc8208ca2d8', '4f4cbca8-e6e8-4eee-b645-77072784f2d8',
                              'ce8004b8-bb07-421d-860a-f2612a0c099c', '8a9d4691-58f4-4d31-858d-bb2c1b819545',
                              '8528cffa-85e8-4d4e-84ef-f95ec6fe53f1']
    }
]
signals = []

fake = Faker()

for query in queries:
    signals_count = randint(10, 5000)
    if query['condition'] == 'Prostate Cancer':
        for i in range(3000):
            signal = {}
            if i % 4 == 0:
                signal['query'] = query['condition'].lower()
            elif i % 3 == 0:
                signal['query'] = query['condition'].title()
            else:
                signal['query'] = query['condition']
            signal['signal_time'] = fake.date_time_between(start_date='-3y', end_date='now').strftime(
                "%Y-%m-%d %H:%M:%S")
            signal['type'] = 'click'
            signal['weight'] = 4
            if i % 3 == 0:
                signal['target'] = ['68db61e5-595a-428f-b5c0-6a1b27c12b4c']
            else:
                signal['target'] = ['ecab8725-fd5a-43dd-a1c0-375b093d660c']
            signals.append(signal)

    for i in range(signals_count):
        switch = randint(0, 2)
        signal = {}
        if i % 4 == 0:
            signal['condition'] = query['condition'].lower()
        elif i % 3 == 0:
            signal['query'] = query['condition'].title()
        else:
            signal['query'] = query['condition']
        signal['signal_time'] = fake.date_time_between(start_date='-3y', end_date='now').strftime("%Y-%m-%d %H:%M:%S")
        if switch == 0:
            signal['type'] = 'click'
            signal['weight'] = 4
        else:
            signal['type'] = ''
            signal['weight'] = 1
        signal['target'] = choice(query['relevantDocuments'])
        signals.append(signal)

shuffle(signals)
print(signals)

with open(f'signals.json', 'w') as f:
    json.dump(signals, f)

"""
connection_bc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Abreast%20cancer&wt=json")
relevantDocument_c = json.load(connection_bc)
for i in relevantDocument_c['response']['docs']:
    query = str(i['brief_title']).lower().replace("\'", "").replace("\'", "").strip()
    condition = str(i['condition']).lower().replace("\'", "").replace("\'", "").strip()
    target = i['id']
    with open(f'signals.json', 'w') as f:
    json.dump(signals, f)
    with open(f'signal_breast_cancer.json) as f:
    json.dump(

"""