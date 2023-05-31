#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import csv
import json
import random
from random import sample
import os
#from gtts import gTTS
#import pandas as pd
#import time

from pathlib import Path
import nltk
import re
from collections import Counter
from nltk import ngrams
#from nltk import sent_tokenize
from nltk import tokenize
import glob


"""

## Modefied corpus_freq FUNC
def corpus_freq(dir_name,lemma_d):
    '''
    To calculate the frequency of a certain 
    Example commands from)
    # 1. https://kristopherkyle.github.io/corpus-analysis-python/Python_Tutorial_4.html
    # 2. The CUPOY NLP course: n-gram tutorial
    '''


    freq = {} #create an empty dictionary to store the word : frequency pairs

    #create a list that includes all files in the dir_name folder that end in ".txt"
    filenames = glob.glob(dir_name + "/*.txt")

    #iterate through each file:
    for filename in filenames:
        #open the file as a string
        text = open(filename, errors = "ignore").read()
        #tokenize text using our tokenize() function
        #tokenized = tokenize(text)
        #lemmatize text using the lemmatize() function
        #lemmatized = lemmatize(tokenized,lemma_d)

        #iterate through the lemmatized text and add words to the frequency dictionary
        for x in lemmatized:
            #the first time we see a particular word we create a key:value pair
            if x not in freq:
                freq[x] = 1
            #when we see a word subsequent times, we add (+=) one to the frequency count
            else:
                freq[x] += 1

    return(freq)
"""


if __name__ == "__main__":
    # Go through all the files
    ## Creat the data path from the folder
    txtRoot_DIR = "/Users/neuroling/Documents/coca/coca-wlp/"
    txtFile_DIR_LIST = []
    for folder in Path(txtRoot_DIR).iterdir():
        if re.match(r'wlp_*', folder.name):
            txtFile_DIR_LIST.append(folder.name)
    pprint(txtFile_DIR_LIST)
    ## Find all txt files
    All_txtNameLIST = []
    for txtFolderSTR in txtFile_DIR_LIST:
        everytxt_DIR_STR = txtRoot_DIR + txtFolderSTR
        filenamesLIST = glob.glob(everytxt_DIR_STR + "/*.txt")
        All_txtNameLIST.extend(filenamesLIST)
    #print(type(All_txtNameLIST))
    print(len(All_txtNameLIST))
    
    all_cleanedLIST = []
    for fileN_STR in filenamesLIST[:3]:
        with open (fileN_STR, errors="ignore", encoding="utf-8") as fileTXT:  # Use all "wlp-" tagged txt files, it contains POS taggings
            rawLIST = fileTXT.read().replace("\t", " ").split("\n")
            pprint(rawLIST[:10])
            print(type(rawLIST))
            print(len(rawLIST))
        cleanedLIST = []
        # Split the tagged txt into LIST
        for rowSTR in rawLIST[:10]:
            tmpLIST = rowSTR.split(" ")
            # remove blurred raw txt, and append the rest of it
            if len(tmpLIST[-1]) == 0:
                pass
            else:
                cleanedLIST.append(tmpLIST)
        pprint(cleanedLIST)
        print(len(cleanedLIST))
        all_cleanedLIST.extend(cleanedLIST)
    pprint(all_cleanedLIST)
    print(len(all_cleanedLIST))
    

    corpus_countDICT = {}
    #iterate through the lemmatized text and add words to the frequency dictionary
    for x in cleanedLIST:
        #the first time we see a particular word we create a key:value pair
        if x not in freq:
            freq[x] = 1
        #when we see a word subsequent times, we add (+=) one to the frequency count
        else:
            freq[x] += 1

            
            
    
    """
    # TRIGRAM ## example commands from the CUPOY NLP course: n-gram tutorial
    
    trigram_frequencyDICT = dict()
    # Starting from the first word(py_index=0), and add 1 to frequency when counted.
    for i in range(0, len(wordLIST)-2):
        trigram_frequencyDICT[tuple(wordLIST[i:i+3])] = trigram_frequencyDICT.get(tuple(wordLIST[i:i+3]), 0) + 1
    # Sorted by the trigram freqeuncy, and formed as (word, count) format.
    trigram_frequencyDICT = sorted(trigram_frequencyDICT.items(), key=lambda words_count: words_count[1], reverse=True)
    # Check the top 10 frequent trigram.
    pprint(trigram_frequencyDICT[:10])
    
    
    # Surprisal calculation (= calculation of the target POS's probability
    # >> calculation theorum == https://vitalflux.com/n-gram-language-models-explained-examples/
    
    #POS_surprisalFLOAT = targetPOS_countINT/prev2w_countINT
    """
