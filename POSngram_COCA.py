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
    
    """
    for fileN_STR in filenamesLIST:
        with open (fileNamesSTR, errors="ignore", encoding="utf-8") as fileTXT:
            fileTXT.read()
    """
    # bigram ## example commands from the CUPOY NLP course: n-gram tutorial
    bigram_frequency = dict()
    
    for i in range(0, len(words)-1):
        bigram_frequency[tuple(words[i:i+2])] = bigram_frequency.get(tuple(words[i:i+2]), 0) + 1
        
    # 根據詞頻排序, 並轉換為(word, count)格式
    bigram_frequency = sorted(bigram_frequency.items(), key=lambda words_count: words_count[1], reverse=True)
    
    # 查看詞頻前10的字詞
    bigram_frequency[:10]        
