import json
import preprocessing
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn import metrics


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

print(len(pattern_list))

CountVec = TfidfVectorizer(stop_words="english")
bag_of_words = CountVec.fit_transform(pattern_list)

X_train ,X_test ,y_train ,y_test = train_test_split(bag_of_words,label_list,test_size=0.2,random_state=233)
#print(type(X_train))

linear_svc_model = LinearSVC(multi_class="ovr")
linear_svc_model.fit(X_train,y_train)
y_pred = linear_svc_model.predict(X_test)

accuracy = metrics.accuracy_score(y_pred,y_test)
confusion_metrix = metrics.confusion_matrix(y_pred,y_test)
print(accuracy)
print(confusion_metrix)
#print(accuracy)


while 1:
	text = str(input(">>"))
	if text == "Quit":
		break
	text = preprocessing.clean_data(text)
	z = CountVec.transform([text])
	#print(linear_svc_model.predict(z))	
	print(data["Intent"][linear_svc_model.predict(z)[0]]['Response'][0])