# BOOKS IN TEXT CAN BE DOWNLOADED HERE
# http://textfiles.com/etext/FICTION/

# SOME EXPLANATIONS ABOUT WORD2VEC ARE GIVEN HERE
# # https://github.com/llSourcell/word_vectors_game_of_thrones-LIVE/blob/master/Thrones2Vec.ipynb
# http://jalammar.github.io/illustrated-word2vec/
# https://radimrehurek.com/gensim/models/word2vec.html


#  IMPORTING MODULES
from __future__ import absolute_import, division, print_function
#for word enconding
import codecs
#regex
import glob
import logging
#concurrency
import multiprocessing
import os
import pprint
#regular expression
import re 
# TWO MODELS RELATED TO WORD2VEC
# CURRENRLY USING BY GENSIM
import word2vec as w2v2
import gensim.models.word2vec as w2v
from gensim.models.word2vec import FAST_VERSION

#
#dimensionality reduction, There is a video on this - visualize dataset easily
import sklearn.manifold
#math
import numpy as np
# plotting
import matplotlib.pyplot as plt 
#parse pandas as pd
import pandas as pd
#visualization
import seaborn as  sns
# TOKENIZER TOOLS

# tokenizer 1
#import spacy # I RATHER USE NLTK

# tokenizer 2
import nltk
# Word Tokenization – Splitting words in a sentence.
from nltk import word_tokenize 
 # PunktWordTokenizer – It doen’t seperates the punctuation from the words.
from nltk import WordPunctTokenizer
# These tokenizers work by separating the words using punctuation and spaces. 
# allowing a user to decide what to do with the punctuations at the time of pre-processing.
from nltk import TreebankWordTokenizer
#from nltk.tokenize import sent_tokenize # ALSO WORKS FINE
from nltk import sent_tokenize # Sentence Tokenization – Splitting sentences in the paragraph

#############################################################
# donwloading files for languange tools
nltk.download("punkt")
nltk.download("stopwords")

#############################################################
# saving path of current directory
path_maindir = os.getcwd()
print ("The current working directory is %s" % path_maindir)

#############################################################
## This piece-of-code reads every lines from txt into individual rows
## and it sepparates cells with \n at end of each cell

#with open ("filetext.txt", "r") as myfile:
#    pickle1_text=myfile.readlines()
#    pickle1_text = str(pickle1_text)

#############################################################
# foldername where data.txt is stored
folderbook = "FOLDER_BOOK"
parth2book = path_maindir + "\\" + folderbook
extension = 'txt'
os.chdir(parth2book)
book_filenames = glob.glob('*.{}'.format(extension))

print("Books.txt in " + folderbook + " = ")
print(book_filenames)

##############################################################
# combining all books.txt into a single file
corpus_raw = u""
for book_filename in book_filenames:
    os.chdir(parth2book)
    print("Reading '{0}'...".format(book_filename))
    with codecs.open(book_filename, "r", "utf-8") as book_file:
        corpus_raw += book_file.read()
    print("Corpus is now {0} characters long".format(len(corpus_raw)))
    print()

#############################################################
os.chdir(path_maindir)

#############################################################
# loading the conjunctions, pronoms etc etc
# OBS: stored at: C:\Users\Fernando\AppData\Roaming\nltk_data\tokenizers\punkt
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#raw_sentences = tokenizer.tokenize(corpus_raw) # OPTION 1

# tested only for English language
raw_sentences = sent_tokenize(corpus_raw) # OPTION 2 (WORK AS GOOD AS OPTION 1)


#convert into a list of words
#remove unnnecessary, split into words, no hyphens
#list of words
def sentence_to_wordlist(raw):
    clean = re.sub("[^a-zA-Z]"," ", raw)
    words = clean.split()
    return words

#sentence where each word is tokenized
sentences = []
for raw_sentence in raw_sentences:
    if len(raw_sentence) > 0:
        sentences.append(sentence_to_wordlist(raw_sentence))

print("###########################################")
print(raw_sentences[5]) # checking a random sentence
print("#")
print("#")
print(sentence_to_wordlist(raw_sentences[5]))
print("###########################################")

##############################################################
# checking total of tokens created in joined books.txt
token_count = sum([len(sentence) for sentence in sentences])
print("The integrated-book corpus contains {0:,} tokens".format(token_count))

# checking last sentence
print("total sentences is: ")
print(len(sentences))
#print("last sentence in corpus is: ")
#index1 = len(sentences) - 1
#print(sentences[index1])
#print(" in this file")
#

#############################################################
# TRAIN WORD2VEC

#ONCE we have vectors
#step 3 - build model
#3 main tasks that vectors help with
#DISTANCE, SIMILARITY, RANKING

# Dimensionality of the resulting word vectors.
#more dimensions, more computationally expensive to train
#but also more accurate
#more dimensions = more generalized
num_features = 300
# Minimum word count threshold.
min_word_count = 8
# Number of cpus
num_workers = multiprocessing.cpu_count()
print("number of cpus = " + str(num_workers))
# Context window length.
context_size = 7

# Downsample setting for frequent words.
#0 - 1e-5 is good for this
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible.
#random number generator
#deterministic, good for debugging
seed = 1

#variables_w2v = w2v.__dict__.keys()
#print(variables_w2v)

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec

model1 = w2v.Word2Vec(
    sentences=sentences,
    sg=1,
    seed=seed,
    workers=num_workers,
    size=num_features,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling
)

variables1 = model1.__dict__.keys()
print("MODEL VARIABLES:")
print(variables1)
model1.save("word2vec.model1")

model1 = Word2Vec.load("word2vec.model1")
#model1.train([["hello", "world"]], total_examples=1, epochs=1) # OKAY
model1.train(sentences, total_examples=1, epochs=1)

word2check1 = 'woman' 
word2check2 = 'man'  
word2check3 = "day"
word2check4 = "night"

word2check1_value = model1[word2check1]
word2check1_value_len = len(word2check1_value)
print("word = " + word2check1 + ": contains ('%s') values" %word2check1_value_len)


# similarity between to close words
similarity_value = model1.wv.similarity(word2check1, word2check2)
print("similary between (" + word2check1 + ") and (" + word2check2 + ") = " + str(similarity_value))

# similary between to identical words
similarity_value = model1.wv.similarity(word2check1, word2check1)
print("similary between (" + word2check1 + ") and (" + word2check1 + ") = " + str(similarity_value))

# similary between to unrelated words
similarity_value = model1.wv.similarity(word2check1, word2check3)
print("similary between (" + word2check1 + ") and (" + word2check3 + ") = " + str(similarity_value))


word_similar = word2check1
most_similar_word = model1.most_similar(word_similar)
print(most_similar_word)

most_similar_word0 = most_similar_word[0][0]
print("WORD (" + word_similar + ") has the most similar word (" + str(most_similar_word[0][0]) + ") and similarity value = " + str(most_similar_word[0][1]))

#print(word2check1 + " has the most similar word = " + most_similar_word)

# Probability of a text under the model:
sentence1 = "The fox jumped over a lazy dog"
#probability_sentence1 = model1.score(["The day".split()])

#print("Probability of sentence (" + sentence1 + " = " + str(probability_sentence1))



#model1.self.wv.similar_by_word(words_test, topn=10, restrict_vocab=None)
#self.wv.similar_by_word(words_test, topn=10, restrict_vocab=None)


#sentences2 = [['first', 'sentence'], ['second', 'sentence']]
#model2 = w2v.Word2Vec(sentences2, size=100, window=5, min_count=1, workers=4)
#model2.save("word2vec.model2")
#model2 = Word2Vec.load("word2vec.model2")
#model2.train([["hello", "world"]], total_examples=1, epochs=1) # OKAY








