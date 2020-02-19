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

from sklearn.feature_extraction.text import TfidfVectorizer

data = []
data_labels = []
with open("animal.txt") as f:
    for i in f: 
        data.append(i) 
        data_labels.append('you are talking about animals')

with open("food.txt") as f:
    for i in f: 
        data.append(i)
        data_labels.append('you are talking about food')

with open("sport.txt") as f:
    for i in f: 
        data.append(i)
        data_labels.append('you are talking about sport')


corpus = data
classes = data_labels
sentence_test = ["I like to play soccer and walk"]

#vectorizer = TfidfVectorizer(min_df=1, max_df=1)
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(corpus)
#X = vectorizer.fit(corpus)
#print("### X[0] ###")
#print(X)

################################################
# MODEL EQUATION OPTIONS !!!!!
################################################
### MODEL 1 ###
from sklearn.svm import LinearSVC
classifier = LinearSVC()

### MODEL 2 ###
# OBS: bad predictions for short sample??
#from sklearn.linear_model import LogisticRegression
#classifier = LogisticRegression() # BAD PREDICTION !!!

### MODEL 3 ###
#from sklearn.naive_bayes import GaussianNB # NOT!!!
#classifier = GaussianNB() # NOT!!!


################################################
# TRAINING MODEL OPTIONS !!!!!
################################################
OPTION_TRAINING = 2

################################################
# OPTION 1 (without training and checking)

classifier = classifier.fit(X, classes)
sentence_test_data = vectorizer.transform(sentence_test)

################################################
# OPTION 2 (with training and checking)

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test  = train_test_split(corpus, classes, test_size = 0.2)

# from sklearn.feature_extraction.text import CountVectorizer
# count = CountVectorizer()
# temp = count.fit_transform(X_train)

# from sklearn.feature_extraction.text import TfidfTransformer
# tdif = TfidfTransformer()
# temp2 = tdif.fit_transform(temp)

# classifier = classifier.fit(temp2, y_train)

# prediction_data = tdif.transform(count.transform(X_test))

# print("########## printing prediction_data MEAN ############")
# predicted = classifier.predict(prediction_data)
# import numpy as np
# print(np.mean(predicted == y_test))

# test_data = tdif.transform(count.transform(test))

################################################

print("### sentence_test ###")
print(sentence_test)
print("### sentence_test_data ###")
print(sentence_test_data)
result1 = classifier.predict(sentence_test_data)
print("### RESULT ###")
print(result1)


import pickle # to save the model
# https://stackoverflow.com/questions/32764991/how-do-i-store-a-tfidfvectorizer-for-future-use-in-scikit-learn
vectorizer = vectorizer
pickle.dump(vectorizer, open("model4vectorizer.pickle", "wb"))
pickle.dump(classifier, open("model4.pickle", "wb"))
