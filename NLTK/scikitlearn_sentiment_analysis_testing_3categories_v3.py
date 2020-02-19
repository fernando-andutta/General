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
from sklearn.svm import LinearSVC

corpus = [
    "I am super good with Java and JEE",
    "I am super good with .NET and C#",
    "I am really good with Python and R",
    "I am really good with C++ and pointers"
    ]

classes = ["java developer", ".net developer", "data scientist", "C++ developer"]

test = ["I think I'm a good developer with really good understanding of .NET"]

#tvect = TfidfVectorizer(min_df=1, max_df=1)
tvect = TfidfVectorizer()

X = tvect.fit_transform(corpus)
#X = tvect.fit(corpus)
#print("### X[0] ###")
#print(X)

classifier = LinearSVC()
classifier.fit(X, classes)

X_test=tvect.transform(test)

print("### test ###")
print(test)
print("### X_test ###")
print(X_test)

result1 = classifier.predict(X_test)



print("### RESULT ###")
print(result1)

# REMEMBER TO SAVE VECTORIZER ALONGSIDE MODEL !!!!1
# https://stackoverflow.com/questions/32764991/how-do-i-store-a-tfidfvectorizer-for-future-use-in-scikit-learn
##############
import pickle # to save the model
vectorizer = tvect
pickle.dump(tvect, open("vectorizer3.pickle", "wb"))
pickle.dump(classifier, open("model3.pickle", "wb"))

