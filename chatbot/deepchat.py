import tensorflow
import json
import preprocessing
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import numpy as np 

data = json.load(open("Intent.json" , 'r'))
#print(data["Intent"])

pattern_list = []#Containing Different Questions
label_list = []# Contain Corresponding lable

for key,value in data["Intent"].items():
	label = key
	patterns=value["Pattern"]

	for pattern in patterns:
		clean_data = preprocessing.clean_data(pattern)
		pattern_list.append(clean_data)
		label_list.append(key)

#print(len(pattern_list))
#print(pattern_list[25])
#print(len(label_list))
#print(label_list[25])

#stop_words="english"

Tfidf= CountVectorizer()
Tfidf_model = Tfidf.fit_transform(pattern_list)

#print(type(Tfidf_model))
print(Tfidf_model.shape[0])
print(Tfidf_model[50])




tenserflow.reset_default_graph()

net = tflearn.input_data(shape=[None,Tfidf_model.shape[0]])
net = tflearn.fully_connected(net ,8)
net = tflearn.fully_connected(net ,8)
net = tflearn.fully_connected(net ,len(set(label_list)),activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(Tfidf_model,label_list,nepoch=1000,batch_size=8,show_metric=True)
model.save("model.tflearn")