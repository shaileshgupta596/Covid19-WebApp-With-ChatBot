from nltk.corpus import stopwords #containing stopwords
from nltk.stem.porter import PorterStemmer # use to fing a core meaning of words 
from nltk.stem.wordnet import WordNetLemmatizer
import re #used for regular expression operation
import os

stopwords = set(stopwords.words("english"))
def clean_data(data): 
    text=data
    #hte line data.shape will return [row size,columnsize ] from which we are taking row size using index 0
    
    #remove @mentions
    rg=re.compile('@[^, ]*\s*')
    text=re.sub(rg," ",text)

    #remove urls
    rg=re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    text=re.sub(rg," ",text)

    #Remove punctuations
    text = re.sub('[^a-zA-Z0-9]', ' ',text)

    #Convert to lowercase
    text = text.lower()

    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)

    # remove special characters and digits
    #text=re.sub("(\\d|\\W)+"," ",text)
    text=re.sub("(\\W)+"," ",text)

    ##Convert to list from string
    text = text.split()

    ##Stemming
    #ps=PorterStemmer()    #Lemmatisation
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if word not in stopwords ]

    text = " ".join(text)

    return text