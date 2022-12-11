from transformers. import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

word = "breast cancer"

token = []
token=tokenizer.delimiter("breast cancer")

print(token)


