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

import pickle # to save the model

model4 = pickle.load(open("model4.pickle", "rb"))
vectorizer = pickle.load(open("vectorizer4.pickle", "rb"))


test = ["I think I'm a good developer with really good understanding of .NET"]

#from sklearn.feature_extraction.text import TfidfVectorizer
#tvect = TfidfVectorizer(min_df=1, max_df=1)
#tvect = TfidfVectorizer()
tvect = vectorizer

### test ###
#["I think I'm a good developer with really good understanding of .NET"]
### X_test ###
#  (0, 10)       0.3021332221975906
#  (0, 8)        0.45647061388710347
#  (0, 5)        0.5789750934885176
#  (0, 2)        0.6042664443951812

#X_test=tvect.transform(test) # sklearn.exceptions.NotFittedError: TfidfVectorizer - Vocabulary wasn't fitted.
#X_test=tvect.fit_transform(test) # ValueError: X has 8 features per sample; expecting 11
X_test=tvect.transform(test) # using saved vectorizer (vectorizer.pickle) !!!!!

##X_test=tvect.fit(test) ## DEFINETLY WRONG!!!
### X_test ###
#TfidfVectorizer(analyzer='word', binary=False, decode_error='strict',
#                dtype=<class 'numpy.float64'>, encoding='utf-8',
#                input='content', lowercase=True, max_df=1.0, max_features=None,
#                min_df=1, ngram_range=(1, 1), norm='l2', preprocessor=None,
#                smooth_idf=True, stop_words=None, strip_accents=None,
#                sublinear_tf=False, token_pattern='(?u)\\b\\w\\w+\\b',
#                tokenizer=None, use_idf=True, vocabulary=None)


print("### test ###")
print(test)
print("### X_test ###")
print(X_test)

    
result1 = model4.predict(X_test) # using saved vectorizer from calibrated model
print("### RESULT ###")
print(result1)