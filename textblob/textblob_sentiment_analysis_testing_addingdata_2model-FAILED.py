# https://textblob.readthedocs.io/en/dev/

# The textblob.sentiments module contains two sentiment analysis implementations:
# 1 - PatternAnalyzer (based on thepatternlibrary) available at https://www.clips.uantwerpen.be/pattern 
# 2 - NaiveBayesAnalyzer (NLTKclassiﬁer trained on a movie reviews corpus).

# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora\movie_reviews
# The default implementation is PatternAnalyzer, but you can override the analyzer
# by passing another implementation into a TextBlob’s constructor.

# DATABASE FOR TEXBLOB IS STORED AT
# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora

#from pathlib import Path as path

# loading needed mobules
import time
# START TIME
t0 = time.time()


train = [
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

train1 = [
('I love this sandwich.', 'pos'),
('this is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('this is my best work.', 'pos'),
("what an awesome view", 'pos')
]

train2 = [

('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('he is my sworn enemy!', 'neg'),
('my boss is horrible.', 'neg')
]


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


    with open('train_part1.json', 'r') as train_file1:
        train_file1 = train1
        model1 = NaiveBayesClassifier(train_file1, format="json")

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
# CREATING A NEUTRAL CLASS FROM POSITIVE AND NEGATIVE
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


model1updated = model1

with open('train_part2.json', 'r') as train_file2:
    train_file2 = train_file2
#    model1updated.update(train_file2) # PROBLEM HERE !!!!!!!!!!!!



# END TIME
t1 = time.time()
total_time = t1-t0
text1 = "total processing time = " + str(total_time) + " seconds"
print(text1)