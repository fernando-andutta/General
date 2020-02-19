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

import pickle
model = pickle.load(open("model4.pickle", "rb"))
vectorizer = pickle.load(open("model4vectorizer.pickle", "rb"))

# your test example
test = ["I like to play soccer and walk"]


### test ###
#["I like to play soccer and walk"]
### X_test ###
#  (0, 10)       0.3021332221975906
#  (0, 8)        0.45647061388710347
#  (0, 5)        0.5789750934885176
#  (0, 2)        0.6042664443951812

# (PROBLEM 1) X_test=vectorizer.transform(test) # sklearn.exceptions.NotFittedError: TfidfVectorizer - Vocabulary wasn't fitted.
# (PROBLEM 2) X_test=vectorizer.fit_transform(test) # ValueError: X has 8 features per sample; expecting 11
X_test=vectorizer.transform(test) # using saved vectorizer (model4vectorizer.pickle) !!!!!

print("### test ###")
print(test)
print("### X_test ###")
print(X_test)
    
result1 = model.predict(X_test) # using saved vectorizer from calibrated model
print("### RESULT ###")
print(result1)