# FOR THIS CODE, I HAVE USED THIS VIDEO
# https://www.youtube.com/watch?v=XrbzmaxjEf0
# AND THIS DATA
# https://github.com/coding-maniacs/sentiment_tut1

# https://stackabuse.com/text-classification-with-python-and-scikit-learn/ (THIS ONE SEEMS A GOOD EXAMPLE!!!)

# REMEMBER TO SAVE VECTORIZER ALONGSIDE MODEL !!!!1
# https://stackoverflow.com/questions/32764991/how-do-i-store-a-tfidfvectorizer-for-future-use-in-scikit-learn

# https://www.twilio.com/blog/2017/12/sentiment-analysis-scikit-learn.html

# CREATING A NEUTRAL CLASS !!!!!!!!!!!!
# https://stackoverflow.com/questions/47317567/sentiment-analysis-with-3-classes-positive-neutral-and-negative

#https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

# DISPLAY RESULTS USING PIE-PLOT (FOR NEUTRAL, POSITIVE AND NEGATIVE)
# https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

# https://scikit-learn.org/stable/supervised_learning.html


import time
# START TIME
t0 = time.time()

import numpy as np
import pandas as pd
import json as j

import pickle # to save the model

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.cross_validation import train_test_split # did not work!!!
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer

tdif = TfidfTransformer()
count = CountVectorizer()


# save the model to disk
filename = 'finalized_model2.sav'
model = pickle.load(open(filename, 'rb'))


#sente1 = "I love love so much this amazing food" # MUST USE BRACKETS
sente1=["I love love so much this amazing food"]

from sklearn.feature_extraction.text import TfidfVectorizer
tvect = TfidfVectorizer(min_df=1, max_df=1)
#sente1data2=tvect.transform(sente1) # PROBLE HERE!!!
#classifier.predict(sente1data2)
#print("###########################")
#print(sente1data2)


vectorizer = CountVectorizer()
sente1data1=vectorizer.fit_transform(sente1)
print("###########################")
print(sente1data1)
#  (0, 2)        2
#  (0, 4)        1
#  (0, 3)        1
#  (0, 5)        1
#  (0, 0)        1
#  (0, 1)        1

print("###########################")
#print(model.predict(tdif.transform(count.transform([sente1data1]))))
#print(model.predict(sente1data1))  # PROBLE HERE!!!

#testing = tdif.transform(count.transform(["I love love so much this amazing food"]))
#print(testing)

#sente1 = "I love love so much this amazing food"
#sente1data1 = tdif.transform(count.transform([sente1]))
#sente1 data =
#  (0, 14994)    0.20660685786317964
#  (0, 13679)    0.25034387933147684
#  (0, 9735)     0.37792478260212614
#  (0, 8864)     0.7080181576699601
#  (0, 5982)     0.25023389471697377
#  (0, 702)      0.4334832100609162

