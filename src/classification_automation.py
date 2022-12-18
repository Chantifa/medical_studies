from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModel, Pipeline
import torch
import json
from urllib.request import urlopen


def getClassification(query):
    model = AutoModelForSequenceClassification.from_pretrained("tarasophia/Bio_ClinicalBERT_medical")
    tokenizer = AutoTokenizer.from_pretrained("tarasophia/Bio_ClinicalBERT")
    inputs = tokenizer(query, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    model.config.id2label[predicted_class_id]
    predicted_token_class_ids = logits.argmax(-1)
    predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
    return predicted_tokens_classes


condition_list = []
token1_text = []
token1_dep = []

# erstellen einer Tabelle von json signals to pandas
connection = urlopen(
    "http://localhost:8983/solr/med_studies/select?defType=lucene&facet.contains=cancer&facet.field=condition&facet.sort=count&facet=true&indent=true&q.op=OR&q=brief_title%3Acancer&wt=json")
response = json.load(connection)

colors = []


# Building the category
def get_cat(response):
    for i in response['response']['docs']:
        condition_list.append(i['condition'])
    df = pd.DataFrame(condition_list)
    print(df[0])
    return df[0]

df = get_cat(response)
def cat_color(response, df):
    condition_list = []
    color = list(np.random.choice(range(256), size=3))
    count = len(df['0'])+1
    colors.append(color)
    for i in response['response']['rows']:
        count = count -1
        if str(i['brief_title']).__contains__(str(df[count]).lower().strip()):
            condition_list.append()



def catogerization(response):
    classLabelVector = []  # categories
    classColorVector = []  # to visualize the cateogires
    index = 0
    cat = get_cat(response)
    list_lenght = len(cat[0])
    returnMat = numpy.zeros(list_lenght - 1,4) # An Numpy-Matrix in high of the rowcount (minus collumn-count)
    for i in response['response']['docs']:
        if str(i['condition']).strip().lower().__contains__(str(cat[0].iterrows())):
            returnMat[index - 1, :] = cat[1:5]
            color = list(np.random.choice(range(256), size=3))
            colors.append(color)
            classLabelVector.append(str(i['condition'].lower().strip()))  # Kategorie als Text-Label speichern
        classColorVector.append(colors)  # categories to save in colors (Cancer = yellow, HIV = red, House = Blue)
        index += 1
    print(classLabelVector)
    print(classColorVector)
    return returnMat, classLabelVector, classColorVector


dataset, classLabelVector, classColorVector = catogerization(get_cat(response))
print(classColorVector)
fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.scatter(dataset[:, 0], dataset[:, 1], marker='o', color=classColorVector)
ax.set_xlabel("count of docs")
ax.set_ylabel("clicks")
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
pyplot.show()

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.scatter(dataset[:, 0], dataset[:, 2], marker='o', color=classColorVector)
ax.set_xlabel("count of docs")
ax.set_ylabel("IA_Ratio")
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
pyplot.show()

fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset[:, 0], dataset[:, 2], dataset[:, 1], marker='o', color=classColorVector)
ax.set_xlabel("count of docs")
ax.set_ylabel("IA_Ratio")
ax.set_zlabel("clicks")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.set_zlim(bottom=0)
pyplot.show()

"""

def normalizeDataSet(dataset):
    dataSet_n = numpy.zeros(numpy.shape(dataset))  

    minValues = dataset.min(0) 
    print(dataset.min)
    ranges = dataset.max(0) - dataset(0) 

    minValues = dataset.min(0) 
    maxValues = dataset.max(0)  

    ranges = maxValues - minValues  

    rowCount = dataset.shape[0] 

    # numpy.tile() wiederholt Sequenzen 

    dataSet_n = dataset - numpy.tile(minValues, (rowCount, 1))

    dataSet_n = dataSet_n / numpy.tile(ranges, (rowCount, 1)) 



dataSet_n, ranges, minValues = normalizeDataSet(dataset)


def classify(inX, dataSet, labels, k):
    rowCount = dataSet.shape[0]  # Anzahl an Zeilen bestimmen
    diffMat = numpy.tile(inX, (rowCount, 1)) - dataSet  # Berechnung der Katheten
    # (über tile() wird der Eingangsdatensatz über die Zeilenanzahl des dataSet vervielfacht, der dataSet davon substrahiert)
    sqDiffMat = diffMat ** 2  # Quadrat der Katheten
    sqDistances = sqDiffMat.sum(axis=1)  # Aufsummieren der Differenzpaare
    distances = sqDistances ** 0.5  # Quadratwurzel über alle Werte
    sortedDistIndicies = distances.argsort()  # Aufsteigende Sortierung
    classCount = {}

    for i in range(k):  # Eingrenzung auf k-Werte in der sortierten Liste
        closest = labels[
            sortedDistIndicies[i]]  # Label (Kategorie [Büro, Wohnung, Haus] entsprechend der Sortierung aufnehmen
        classCount[closest] = classCount.get(closest, 0) + 1  # Aufbau eines Dictionary über die
        sortedClassCount = sorted(classCount, key=classCount.get, reverse=True)
    return sortedClassCount[0]  

errorCount = 0

k = 5  # k-limit 

rowCount = dataSet_n.shape[0]  # Anzahl der Zeilen im gesamten Datensatz

numTestVectors = 30 
for i in range(0, numTestVectors):  
    result = classify(dataSet_n[i, :], dataSet_n[numTestVectors:rowCount, :], classLabelVector[numTestVectors:rowCount],
                      k)
    print("%s - the classifier came back with: %s, the real answer is: %s" % (i, result, classLabelVector[i]))

    if (result != classLabelVector[i]):
        errorCount += 1.0
print("Error Count: %d" % errorCount)
"""
