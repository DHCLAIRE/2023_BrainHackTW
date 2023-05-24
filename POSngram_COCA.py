#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import csv
import json
import random
from random import sample
import os
#from gtts import gTTS
import pandas as pd
import time
from pathlib import Path
import nltk
import re
#from nltk import sent_tokenize
#from nltk import tokenize
import glob


# Command examples from https://kristopherkyle.github.io/corpus-analysis-python/Python_Tutorial_4.html
def corpus_freq(dir_name,lemma_d):
    freq = {} #create an empty dictionary to store the word : frequency pairs

    #create a list that includes all files in the dir_name folder that end in ".txt"
    filenames = glob.glob(dir_name + "/*.txt")

    #iterate through each file:
    for filename in filenames:
        #open the file as a string
        text = open(filename, errors = "ignore").read()
        #tokenize text using our tokenize() function
        tokenized = tokenize(text)
        #lemmatize text using the lemmatize() function
        lemmatized = lemmatize(tokenized,lemma_d)

        #iterate through the lemmatized text and add words to the frequency dictionary
        for x in lemmatized:
            #the first time we see a particular word we create a key:value pair
            if x not in freq:
                freq[x] = 1
            #when we see a word subsequent times, we add (+=) one to the frequency count
            else:
                freq[x] += 1

    return(freq)

if __name__ == "__main__":
    # Go through all the files
    txt_DIR = "/Users/neuroling/Documents/coca/coca-wlp/wlp_acad_vuw"
    filenamesLIST = glob.glob(txt_DIR +"/*.txt")
    print(type(filenamesLIST))
    print(len(filenamesLIST))
    
    for fileN_STR in filenamesLIST:
        with open (fileNamesSTR, errors="ignore", encoding="utf-8") as fileTXT:
            fileTXT.read()
            
        
    