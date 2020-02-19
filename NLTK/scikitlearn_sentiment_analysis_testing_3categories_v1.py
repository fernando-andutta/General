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


from sklearn.feature_extraction.text import CountVectorizer

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

vectorizer = CountVectorizer(analyzer = 'word', lowercase = False)

features = vectorizer.fit_transform(data)

features_nd = features.toarray() # for easy usage

#from sklearn.cross_validation import train_test_split # did not work!!!
from sklearn.model_selection import train_test_split

#X_train, X_test, y_train, y_test  = train_test_split(
#        features_nd, 
#        data_labels,
#        train_size=0.80, 
#        random_state=1234)
X_train, X_test, y_train, y_test  = train_test_split(features_nd, data_labels, train_size=0.80, random_state=1234)


from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

n = 0
X_train_str = str(X_train[n])
print("X_train[" + str(n) + "] = " + X_train_str)
y_train_str = str(y_train[n])
print("Y_train[" + str(n) + "] = " + y_train_str)


y_pred = log_model.predict(X_test)

n = 0
X_test_str = str(X_test[n])
print("X_test[" + str(n) + "] = " + X_test_str)
y_test_str = str(y_test[n])
print("Y_test[" + str(n) + "] = " + y_test_str)

from sklearn.feature_extraction.text import TfidfTransformer
tdif = TfidfTransformer()
count = CountVectorizer()
#print(log_model.predict(tdif.transform(count.transform(["I have a dog"])))) # PROBLEM HERE!!!!
