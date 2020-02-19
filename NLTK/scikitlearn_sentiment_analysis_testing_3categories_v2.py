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


json_data = None
with open("yelp_academic_dataset_review.json") as data_file:
    lines = data_file.readlines()
    joined_lines = "[" + ",".join(lines) + "]"

    json_data = j.loads(joined_lines)

data = pd.DataFrame(json_data)
data.head()

#data = data[data.stars !=3]
#data['sentiment'] = data['stars'] >= 4


data["sentiment"] = "EMPTY"


data_rows = len(data)
print("data_rows = " + str(data_rows))

for i in range(0, data_rows):
    date_star_row = data.stars[i]
    if date_star_row > 4:
        data.sentiment[i] = "POSITIVE"
    elif date_star_row <= 4 and date_star_row >= 3:
        data.sentiment[i] = "NEUTRAL"
    elif date_star_row < 3:
        data.sentiment[i] = "NEGATIVE"


#data.sentiment = str(data.sentiment)

data.head()

print("#####################################")
print(data.stars[0:20])
print("#####################################")
print(data.sentiment[0:20])
print("#####################################")


X_train, X_test, y_train, y_test  = train_test_split(data, data.sentiment, test_size = 0.2)

print("########## X_test ############")
print(X_test[0:2])

count = CountVectorizer()
temp = count.fit_transform(X_train.text)

tdif = TfidfTransformer()
temp2 = tdif.fit_transform(temp)

text_regression = LogisticRegression()

model = text_regression.fit(temp2, y_train)

prediction_data = tdif.transform(count.transform(X_test.text))

print("########## printing prediction_data ############")
print(prediction_data[0])

print("########## printing prediction_data MEAN ############")
predicted = model.predict(prediction_data)
print(np.mean(predicted == y_test))

print("########## printing example sentences ############")

sente1 = "I love love so much this amazing food"
sente1data1 = tdif.transform(count.transform([sente1]))
print("sente1 = " + str(sente1))
print("sente1 data = ")
print(sente1data1)
print("###########################")
#print(model.predict(tdif.transform(count.transform([sente1data1]))))
print(model.predict(sente1data1))

#sente1 = "I love love so much this amazing food"
#sente2 = "this is a good movie"
#sente3 = "I hated so much this food, it was disgusting, never again."



# END TIME  
t1 = time.time()
total_time = t1-t0
text1 = "total processing time = " + str(total_time) + " seconds"
print(text1)
