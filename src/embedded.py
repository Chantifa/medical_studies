import json
from urllib.request import urlopen

import sns as sns
from pandas.io.common import urlopen
from transformers import AutoTokenizer, AutoModel
import pandas as pd
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

word = "breast cancer"

connection_bc = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=cancer&facet.field=official_title&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Abreast%20cancer&wt=json")
relevantDocument_bc = json.load(connection_bc)

seq_len_premise = [len(i.split()) for i in relevantDocument_bc['doc']]

for i in relevantDocument_bc['response']['doc']:
    i.split
pd.Series(seq_len_premise).hist(bins = 25)
sns.countplot(context['context'])
# Obtain a 10% test set from train set
X_train_Transformer, X_val_Transformer, y_train_Transformer, y_val_Transformer = train_test_split(
                                                    x_train, y_train, test_size=0.20, random_state=42)