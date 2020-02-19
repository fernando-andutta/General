# https://textblob.readthedocs.io/en/dev/

# The textblob.sentiments module contains two sentiment analysis implementations:
# 1 - PatternAnalyzer (based on thepatternlibrary) available at https://www.clips.uantwerpen.be/pattern 
# 2 - NaiveBayesAnalyzer (NLTKclassiﬁer trained on a movie reviews corpus).

# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora\movie_reviews (CHECK YOUR USERNAME FOR LOCATION!!!)
# The default implementation is PatternAnalyzer, but you can override the analyzer
# by passing another implementation into a TextBlob’s constructor.

# DATABASE FOR TEXBLOB IS STORED AT
# C:\Users\Fernando\AppData\Roaming\nltk_data\corpora (CHECK YOUR USERNAME FOR LOCATION!!!)


import time
# START TIME
t0 = time.time()

model_name = "model_v2.pickle"

try:
    f1 = open(model_name)
    print("Model exists, and going to be considered.")

    #############################################################
    # LOADING THE MODEL CALIBRATED
    #############################################################

    import pickle
    f1 = open(model_name, 'rb')
    model = pickle.load(f1)
    f1.close()

except IOError:

    print("Model does not exist, so we are generating a new one.")

    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer
    from textblob.sentiments import PatternAnalyzer
    from textblob.classifiers import NaiveBayesClassifier


    with open('train.json', 'r') as train_file:
        model = NaiveBayesClassifier(train_file, format="json")

    #############################################################
    # SAVING THE MODEL CALIBRATED
    #############################################################
    import pickle
    f = open(model_name, 'wb')
    pickle.dump(model, f)
    f.close()

finally:
    print("Model has just being loaded, and ready to be used.")
    print("#################################################")
    print("##################  MODEL  ######################")

with open('test.json', 'r') as test_file:
    model_accuracy = model.accuracy(test_file, format=None)
    print("model accuray = '%s' " %model_accuracy)


###############################################################################
# CREATING A NEUTRAL CLASS FROM POSITIVE AND NEGATIVE
###############################################################################

print("#################################################")


text3 = "We did not like his results."
#probability_classification_chosen = 'neg'
#probability_positive = '0.11'
#probability_negative = '0.89'

print("Assessing text = " + text3)
model_prob_dist = model.prob_classify(text3)
#probability_classification_chosen = model_prob_dist.max()
#print("probability_classification = '%s' " %probability_classification_chosen)

probability_positive = round(model_prob_dist.prob("pos"), 2)
#print("probability_positive = '%s' " %probability_positive)

probability_negative = round(model_prob_dist.prob("neg"), 2)
#print("probability_negative = '%s' " %probability_negative)

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
    probability_classification_chosen2 = "Model could not properly classified your text."
    print("probability_positive = '%s' " %probability_positive)
    print("probability_negative = '%s' " %probability_negative)
else:
    print("probability_classification = '%s' " %text_classification)



# END TIME
t1 = time.time()
total_time = t1-t0
text1 = "total processing time = " + str(total_time) + " seconds"
print(text1)