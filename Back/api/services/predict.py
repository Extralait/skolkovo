import pickle

from bs4 import BeautifulSoup as bs
import mailbox
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

import nltk.corpus

nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
from random import randint
from Config.settings import BASE_DIR


model_path = os.path.join(BASE_DIR, "api/services/model1.pkl")
print(model_path)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

stop = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def predict(from_email,to_email,date,content_type,x_uid,body, subject):

    content = body
    content = pd.Series(content)
    content = content.str.lower()
    content = content.apply(lambda x: re.sub(r'[\W\d]', " ", x))
    content = content.apply(
        lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split() if word not in (stop)]))
    content = content.apply(lambda x: " ".join([word for word in x.split() if len(word) > 2]))

    pred = model.predict_proba(content)[0, 1]

    return int(pred >= 0.85), pred

