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
#import time

from pathlib import Path
import nltk
import re
from collections import Counter, defaultdict
from nltk import ngrams
from nltk import trigrams
#from nltk import sent_tokenize
from nltk import tokenize
import glob
import math


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
    taggedRoot_DIR_STR = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_MEG/"
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
    all_POStagLIST = []
    for fileN_STR in filenamesLIST[:10]:
        print(fileN_STR)
        with open (fileN_STR, errors="ignore", encoding="utf-8") as fileTXT:  # Use all "wlp-" tagged txt files, it contains POS taggings
            rawLIST = fileTXT.read().replace("\t", " ").split("\n")
            #pprint(rawLIST)#[:50])
            #print(type(rawLIST))
            #print(len(rawLIST))
        cleanedLIST = []
        POStagLIST = []
        # Split the tagged txt into LIST
        for rowSTR in rawLIST[:50]:
            tmpLIST = rowSTR.split(" ")
            # remove blurred raw txt, and append the rest of it
            if len(tmpLIST[-1]) == 0:
                pass
            else:
                cleanedLIST.append(tmpLIST)
                POStagLIST.append(tmpLIST[-1])
        #pprint(cleanedLIST)
        #print(len(cleanedLIST))
        #print(POStagLIST)
        all_cleanedLIST.append(cleanedLIST)
        all_POStagLIST.append(POStagLIST)
        
    #pprint(all_cleanedLIST)
    #print(len(all_cleanedLIST))
    #pprint(all_POStagLIST)
    #print(len(all_POStagLIST))
    
    
    corpus_freqDICT = defaultdict(lambda: defaultdict(lambda: 0))
    # Count frequency of co-occurance ## example script from https://alvinntnu.github.io/python-notes/nlp/language-model.html
    for posLIST in all_POStagLIST:
        ''' # use it later
        print(posLIST)
        trigramLIST = list(nltk.ngrams(posLIST, 3))
        print(trigramLIST[:3])
        '''
        for pos1, pos2, pos3 in trigrams(posLIST, pad_right=True, pad_left=True):
                corpus_freqDICT[(pos1, pos2)][pos3] += 1
        
    # Let's transform the counts to probabilities
    for pos1_pos2 in corpus_freqDICT:
        total_count = float(sum(corpus_freqDICT[pos1_pos2].values()))
        for pos3 in corpus_freqDICT[pos1_pos2]:
            corpus_freqDICT[pos1_pos2][pos3] /= total_count
            #print(type(corpus_freqDICT))
            #pprint(corpus_freqDICT)
    
    # Load in the sub's POS tagged jsonfile
    with open (taggedRoot_DIR_STR + "S007_dePOS_LIST.json", "r", encoding = "utf-8") as jfile:
        sub_posLIST = json.load(jfile)
        pprint(sub_posLIST)
        blankPOSLIST = []
        for n_posLIST in sub_posLIST:
            blankPOSLIST.append(n_posLIST[-1])
            trigramLIST = list(nltk.ngrams(posLIST, 3))
            print()
    
    """
    #testingLIST = [['vvi', 'appge'], ['nn2', 'vbdr'], ['np1', 'cc']]  #[('nn1', 0.6666666666666666), ('jj', 0.3333333333333333)] ; [('jj', 1.0)] ; [('np1', 0.6666666666666666), ('pphs1', 0.3333333333333333)]
    ans_LIST = [['vvi', 'appge', 'nn1'], ['nn2', 'vbdr', 'jj'], ['np1', 'cc', 'np1']]
    # Calculated the surprisal from trained COCA corpus
    surprisalLIST = []
    for targetPOS_LIST in ans_LIST:
        # Get the probabilities from the trigram model (trained by COCA)  'nn2', 'vbdr'
        freqResultDICT = sorted(dict(corpus_freqDICT[targetPOS_LIST[0], targetPOS_LIST[1]]).items(), key=lambda x:-1*x[1])
        #print(freqResultDICT, type(freqResultDICT)) # lIST = [('nn1', 0.6666666666666666), ('jj', 0.3333333333333333)]
        #print(freqResultDICT[0], type(freqResultDICT[0])) #tuple = ('nn1', 0.6666666666666666)
        #print(freqResultDICT[0][1], type(freqResultDICT[0][1])) #float = 1.0
        
        # Match the wanted trigram to its following 
        for posTUPLE in freqResultDICT:
            print("HII__", posTUPLE)
            posSTR = posTUPLE[0]
            print("NOW:", posSTR)
            if posSTR == targetPOS_LIST[-1]:
                probFLOAT = posTUPLE[1]
                print(targetPOS_LIST[-1], posSTR)
            else:
                print("NADA")

        # log2 to get the surprisal from probabilites
        surprisal_triFLOAT = float(math.log2(probFLOAT))
        surprisalLIST.append(surprisal_triFLOAT)
    
    dataDICT = pd.DataFrame({#'Word':Word_LIST,
                           'NGRAM':surprisalLIST
                           })
                           
    #data_path = "/Users/ting-hsin/Docs/Github/ICN_related/"
    file_name = 'S007_Ngram_predictor.csv'
    save_path = taggedRoot_DIR_STR + file_name
    dataDICT.to_csv(save_path, sep = "," ,index = False , header = True, encoding = "UTF-8")
    """
            
################### REDUNDANT ##########
    """
        #the first time we see a particular word we create a key:value pair
        if infoLIST[1] not in corpus_freqDICT:
            corpus_freqDICT[infoLIST[1]] = 1
        #when we see a word subsequent times, we add (+=) one to the frequency count
        else:
            corpus_freqDICT[infoLIST[1]] += 1
    """
    
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
    # >> calculation theorum == https://vitalflux.com/n-gram-language-corpus_freqDICTs-explained-examples/
    
    #POS_surprisalFLOAT = targetPOS_countINT/prev2w_countINT
    
    # suprisal = -log2(P(w|C)
    """
