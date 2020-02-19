# https://textblob.readthedocs.io/en/dev/

# The textblob.sentiments module contains two sentiment analysis implementations:
# 1 - PatternAnalyzer (based on thepatternlibrary) available at https://www.clips.uantwerpen.be/pattern 
# 2 - NaiveBayesAnalyzer (NLTKclassiﬁer trained on a movie reviews corpus).

# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora\movie_reviews (CHECK YOUR USERNAME FOR LOCATION!!!)
# The default implementation is PatternAnalyzer, but you can override the analyzer
# by passing another implementation into a TextBlob’s constructor.

# DATABASE FOR TEXBLOB IS STORED AT
# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora (CHECK YOUR USERNAME FOR LOCATION!!!)

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.sentiments import PatternAnalyzer
from textblob.classifiers import NaiveBayesClassifier

text = '''
PLACE PARAGRAPH HERE
'''
# text = '''
# The titular threat of The Blob has always struck me as the ultimate movie
# monster: an insatiably hungry, amoeba-like mass able to penetrate
# virtually any safeguard, capable of--as a doomed doctor chillingly
# describes it--"assimilating flesh on contact.
# Snide comparisons to gelatin be damned, it's a concept with the most
# devastating of potential consequences, not unlike the grey goo scenario
# proposed by technological theorists fearful of
# artificial intelligence run rampant.
# '''

#text1 = "Results were found in agreement with reports by Dantes et al 2019." # NEGATIVE
#text1 = "I am very happy with her research findings." # POSITIVE
#text1 = "We have confirmed previous observation by Andutta et al 2014." # NEGATIVE
text1 = "We have confirmed previous observation by Andutta et al 2014. We disagree with Andutta research findings, and wish to highlight here. We believe these findings to be wrong." # NEGATIVE

print("###################################################################")
print("############  MODEL 1  ###############")
model1= TextBlob(text1, analyzer=PatternAnalyzer()) # USE THIS FOR PatternAnalyzer
#model1 = TextBlob(text1) # USE THIS FOR PatternAnalyzer (BY DEFAULT)
# We disagree with Fernando Andutta's research findings, and wish to highlight here.
# Polarity = '0.0'
# Subjectivity = '0.0'

xx = 0
for sentence in model1.sentences:
    xx = xx+1
    print("###################################")
    print("SENTENCE = '%s' " %xx)
    print(sentence)
    #print("sentence = " + sentence)
    #print(sentence.sentiment.polarity) # it shows only polarity
    #print(sentence.sentiment) # it shows polarity and subjectivity
    res1 = sentence.sentiment
    res_polarity = res1[0]
    res_subjectivity= res1[1]
    print("Polarity = '%s' " %res_polarity)
    print("Subjectivity = '%s' " %res_subjectivity)


#blob.translate(to="es")  # 'La amenaza titular de The Blob...'
#print(TextBlob(text).sentiment)



print("###################################################################")
print("############  MODEL 2  ###############")
model2 = TextBlob(text1, analyzer=NaiveBayesAnalyzer()) # USE THIS FOR NaiveBayesAnalyzer
# We disagree with Andutta research findings, and wish to highlight here.
# Polarity = 'neg'
# Subjectivity = '0.44760860969048066'

#model2.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

#model2.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

xx = 0
for sentence in model2.sentences:
    xx = xx+1
    print("###################################")
    print("SENTENCE = '%s' " %xx)
    print(sentence)
    #print("sentence = " + sentence)
    #print(sentence.sentiment.polarity) # it shows only polarity
    #print(sentence.sentiment) # it shows polarity and subjectivity
    res1 = sentence.sentiment
    res_polarity = res1[0]
    res_subjectivity= res1[1]
    print("Polarity = '%s' " %res_polarity)
    print("Subjectivity = '%s' " %res_subjectivity)


# https://textblob.readthedocs.io/en/dev/classifiers.html
train1 = [
('I love this sandwich.', 'pos'),
('this is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('this is my best work.', 'pos'),
("what an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('he is my sworn enemy!', 'neg'),
('my boss is horrible.', 'neg'),
('I can eat this bread.', 'neg'),
('I can eat this bread.', 'pos')
]

test1 = [
('the beer was good.', 'pos'),
('I do not enjoy my job', 'neg'),
("I ain't feeling dandy today.", 'neg'),
("I feel amazing!", 'pos'),
('Gary is a friend of mine.', 'pos'),
("I can't believe I'm doing this.", 'neg')
]

print("###################################################################")
print("############  MODEL 3  ###############")
model3 = NaiveBayesClassifier(train1)

#test2 = "This is an amazing library!"

model3_accuracy = model3.accuracy(test1, format=None)
print("model3 accuray = '%s' " %model3_accuracy)

#text2 = "these results are wrong."
text2 = "I can eat this bread." # expected NEUTRAL PIECE

model3_classify = model3.classify(text2)
print("sentence classified = '%s' " %model3_classify)


model3_prob_dist = model3.prob_classify(text2)
probability_classification_chosen = model3_prob_dist.max()
print("probability_classification_chosen = '%s' " %probability_classification_chosen)

probability_positive = round(model3_prob_dist.prob("pos"), 2)
print("probability_positive = '%s' " %probability_positive)

probability_negative = round(model3_prob_dist.prob("neg"), 2)
print("probability_negative = '%s' " %probability_negative)




print("###################################################################")
print("############  MODEL 4  ###############")
with open('train.json', 'r') as train_file:
    model4 = NaiveBayesClassifier(train_file, format="json")

with open('test.json', 'r') as test_file:
    model4_accuracy = model4.accuracy(test_file, format=None)
print("model4 accuray = '%s' " %model4_accuracy)

###############################################################################
# CREATING A NEUTRAL CLASS FROM POSITIVE AND NEGATIVE
#########################################################   ######################

print("###################################################################")
print("############  MODEL 4 (NEUTRAL)  ###############")

#  https://stackoverflow.com/questions/59498416/textblob-naive-bayes-classifier-for-neutral-tweets
#If you have only two classes, Positive and Negative, and you want to predict if a tweet is Neutral, you can do so by predicting class probabilities.
#For example, a tweet predicted as 80% Positive remains Postive. However, a tweet predicting as 50% Postive could be Neutral instead.
 
# https://textblob.readthedocs.io/en/dev/classifiers.html
#You can get the label probability distribution with the prob_classify(text) method.

#text3 = "This one's a doozy."
#probability_classification_chosen = 'pos'
#probability_positive = '0.63'
#probability_negative = '0.37'

#text3 = "We have used Ridd 2019 data in our test."
#probability_classification_chosen = 'pos'
#probability_positive = '0.63'
#probability_negative = '0.37'

#text3 = "We found these results to be wrong."
#probability_classification_chosen = 'pos'
#probability_positive = '0.86'
#probability_negative = '0.14'

text3 = "We did not like his results."
#probability_classification_chosen = 'neg'
#probability_positive = '0.11'
#probability_negative = '0.89'

model4_prob_dist = model4.prob_classify(text3)
probability_classification_chosen = model4_prob_dist.max()
print("probability_classification_chosen = '%s' " %probability_classification_chosen)

probability_positive = round(model4_prob_dist.prob("pos"), 2)
print("probability_positive = '%s' " %probability_positive)

probability_negative = round(model4_prob_dist.prob("neg"), 2)
print("probability_negative = '%s' " %probability_negative)

#################################################################################
# UPDATING CLASSIFIERS WITH NEW DATA
#################################################################################

#Use the update(new_data) method to update a classifier with new training data.
#You must be consistent with format applied to both data in script of from loaded files

new_data1 = [('She is my best friend.', 'pos'),
("I'm happy to have a new friend.", 'pos'),
("Stay thirsty, my friend.", 'pos'),
("He ain't from around here.", 'neg')]

new_data2 = [{"text": "She is my best friend.", "label": "pos"},
{"text": "I'm happy to have a new friend.", "label": "pos"},
{"text": "Stay thirsty, my friend.", "label": "pos"},
{"text": "He ain't from around here.", "label": "neg"}
]

model3updated = model3
model3updated.update(new_data1)

model4updated = model4
model4updated.update(new_data2)
#model4_accuracy = model4.accuracy(test_file, format=None) ### PROBLEM HERE !!!
#print("model4 accuray = '%s' " %model4_accuracy)


