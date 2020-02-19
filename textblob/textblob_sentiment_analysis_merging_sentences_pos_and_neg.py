# https://textblob.readthedocs.io/en/dev/

# The textblob.sentiments module contains two sentiment analysis implementations:
# 1 - PatternAnalyzer (based on thepatternlibrary) available at https://www.clips.uantwerpen.be/pattern 
# 2 - NaiveBayesAnalyzer (NLTKclassiﬁer trained on a movie reviews corpus).

# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora\movie_reviews (CHECK YOUR USERNAME FOR LOCATION!!!)
# The default implementation is PatternAnalyzer, but you can override the analyzer
# by passing another implementation into a TextBlob’s constructor.

# DATABASE FOR TEXBLOB IS STORED AT
# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora (CHECK YOUR USERNAME FOR LOCATION!!!)

# loading needed mobules
import time
# START TIME
t0 = time.time()


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
#model1 accuray = '0.8333333333333334'
#Assessing text = We did not like his results.
#probability_classification = 'neg'
#probability_positive = '0.12'
#probability_negative = '0.88'

train2 = [
("I love this sandwich. this is an amazing place! I feel very good about these beers. this is my best work. what an awesome view.", 'pos'),
("I do not like this restaurant. I am tired of this stuff. I can't deal with this. he is my sworn enemy! my boss is horrible.", 'neg')
]
#model2 accuray = '0.8333333333333334'
#Assessing text = We did not like his results.
#probability_classification = 'neg'
#probability_positive = '0.04'
#probability_negative = '0.96'

train3 = [
("I love this sandwich. this is an amazing place! I feel very good about these beers.", 'pos'),
("this is my best work. what an awesome view.", 'pos'),
("I do not like this restaurant. I am tired of this stuff.", 'neg'),
("I can't deal with this. he is my sworn enemy! my boss is horrible.", 'neg')
]
#model2 accuray = '0.8333333333333334'
#Assessing text = We did not like his results.
#probability_classification = 'neg'
#probability_positive = '0.02'
#probability_negative = '0.98'

train4 = [
("I love this sandwich. this is an amazing place!", 'pos'),
("I feel very good about these beers. this is my best work. what an awesome view.", 'pos'),
("I do not like this restaurant. I am tired of this stuff. I can't deal with this. ", 'neg'),
("he is my sworn enemy! my boss is horrible.", 'neg')
]
#model2 accuray = '0.6666666666666666'
#################################################
#Assessing text = We did not like his results.
#probability_classification = 'neg'
#probability_positive = '0.0'
#probability_negative = '1.0'

train5 = [
("this is an amazing place! I love this sandwich.", 'pos'),
(" what an awesome view. I feel very good about these beers. this is my best work.", 'pos'),
(" I can't deal with this. I do not like this restaurant. I am tired of this stuff.", 'neg'),
("my boss is horrible. he is my sworn enemy!", 'neg')
]
#model2 accuray = '0.6666666666666666'
#Assessing text = We did not like his results.
#probability_classification = 'neg'
#probability_positive = '0.0'
#probability_negative = '1.0'

train2 = train5


model1_name = "model1.pickle"

try:
    f1 = open(model1_name)
    print("model1 exists, and going to be considered.")

    #############################################################
    # LOADING THE MODEL CALIBRATED
    #############################################################

    import pickle
    f1 = open(model1_name, 'rb')
    model1 = pickle.load(f1)
    f1.close()

except IOError:

    print("model1 does not exist, so we are generating a new one.")

    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer
    from textblob.sentiments import PatternAnalyzer
    from textblob.classifiers import NaiveBayesClassifier


    with open('train_part1.json', 'r') as train_file:
        train_file = train1
        model1 = NaiveBayesClassifier(train_file, format="json")

    #############################################################
    # SAVING THE MODEL CALIBRATED
    #############################################################
    import pickle
    f = open(model1_name, 'wb')
    pickle.dump(model1, f)
    f.close()

finally:
    print("model1 has just being loaded, and ready to be used.")
    print("#################################################")
    print("##################  model1  ######################")

with open('test.json', 'r') as test_file:
    model1_accuracy = model1.accuracy(test_file, format=None)
    print("model1 accuray = '%s' " %model1_accuracy)


###############################################################################
###############################################################################

print("#################################################")
text3 = "We did not like his results."
#probability_classification_chosen = 'neg'
#probability_positive = '0.11'
#probability_negative = '0.89'

print("Assessing text = " + text3)
model1_prob_dist = model1.prob_classify(text3)
probability_classification_chosen = model1_prob_dist.max()
print("probability_classification = '%s' " %probability_classification_chosen)

probability_positive = round(model1_prob_dist.prob("pos"), 2)
print("probability_positive = '%s' " %probability_positive)

probability_negative = round(model1_prob_dist.prob("neg"), 2)
print("probability_negative = '%s' " %probability_negative)

text_classification = "NOT-PROPERLY-CLASSIFIED"
if probability_positive<=0.55 and probability_negative<=0.55:
    text_classification = "NEUTRAL"

elif probability_positive>0.55 and probability_positive<=0.75 and probability_negative<=0.55:
    text_classification = "SLIGHTLY-POSITIVE"
elif probability_positive>0.75 and probability_negative<=0.55:
    text_classification = "HIGLY-POSITIVE"

elif probability_negative>0.55 and probability_negative<=0.75 and probability_positive<=0.55:
    text_classification = "SLIGHTLY-NEGATIVE"
elif probability_negative>0.75 and probability_positive<=0.55:
    text_classification = "HIGLY-NEGATIVE"

if "NOT-PROPERLY-CLASSIFIED" in text_classification:
    probability_classification_chosen2 = "model1 could not properly classified your text."
    #print("probability_positive = '%s' " %probability_positive)
    #print("probability_negative = '%s' " %probability_negative)
else:
    print("probability_classification = '%s' " %text_classification)


model2_name = "model2.pickle"

try:
    f1 = open(model2_name)
    print("model2 exists, and going to be considered.")

    #############################################################
    # LOADING THE MODEL CALIBRATED
    #############################################################

    import pickle
    f1 = open(model2_name, 'rb')
    model2 = pickle.load(f1)
    f1.close()

except IOError:

    print("model2 does not exist, so we are generating a new one.")

    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer
    from textblob.sentiments import PatternAnalyzer
    from textblob.classifiers import NaiveBayesClassifier


    with open('train_part2.json', 'r') as train_file:
        train_file = train2
        model2 = NaiveBayesClassifier(train_file, format="json")

    #############################################################
    # SAVING THE MODEL CALIBRATED
    #############################################################
    import pickle
    f = open(model2_name, 'wb')
    pickle.dump(model2, f)
    f.close()

finally:
    print("model2 has just being loaded, and ready to be used.")
    print("#################################################")
    print("##################  model2  ######################")

with open('test.json', 'r') as test_file:
    model2_accuracy = model2.accuracy(test_file, format=None)
    print("model2 accuray = '%s' " %model2_accuracy)


###############################################################################
###############################################################################

print("#################################################")
text3 = "We did not like his results."
#probability_classification_chosen = 'neg'
#probability_positive = '0.11'
#probability_negative = '0.89'

print("Assessing text = " + text3)
model2_prob_dist = model2.prob_classify(text3)
probability_classification_chosen = model2_prob_dist.max()
print("probability_classification = '%s' " %probability_classification_chosen)

probability_positive = round(model2_prob_dist.prob("pos"), 2)
print("probability_positive = '%s' " %probability_positive)

probability_negative = round(model2_prob_dist.prob("neg"), 2)
print("probability_negative = '%s' " %probability_negative)

text_classification = "NOT-PROPERLY-CLASSIFIED"
if probability_positive<=0.55 and probability_negative<=0.55:
    text_classification = "NEUTRAL"

elif probability_positive>0.55 and probability_positive<=0.75 and probability_negative<=0.55:
    text_classification = "SLIGHTLY-POSITIVE"
elif probability_positive>0.75 and probability_negative<=0.55:
    text_classification = "HIGLY-POSITIVE"

elif probability_negative>0.55 and probability_negative<=0.75 and probability_positive<=0.55:
    text_classification = "SLIGHTLY-NEGATIVE"
elif probability_negative>0.75 and probability_positive<=0.55:
    text_classification = "HIGLY-NEGATIVE"

if "NOT-PROPERLY-CLASSIFIED" in text_classification:
    probability_classification_chosen2 = "model2 could not properly classified your text."
    #print("probability_positive = '%s' " %probability_positive)
    #print("probability_negative = '%s' " %probability_negative)
else:
    print("probability_classification = '%s' " %text_classification)


# END TIME
t1 = time.time()
total_time = t1-t0
text1 = "total processing time = " + str(total_time) + " seconds"
print(text1)