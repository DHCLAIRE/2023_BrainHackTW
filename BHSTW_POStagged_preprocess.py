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

def space2comma(strLIST):
    '''
    Turn the space within the string into comma
    '''
    turedLIST = []
    for elementSTR in strLIST:
        turedLIST.extend(elementSTR.split(" "))
        #print(turedLIST)
    return turedLIST


if __name__ == "__main__":
    
    txtRoot_DIR_STR = "/Volumes/Neurolang_1/Project_Assistant/2021_Ongoing/2020_LTTC/Experiment_materials/LTTC_MEG/"
    POStaggedFolder = txtRoot_DIR_STR + "LTTC_Stim_POStagged"
    #print(POStaggedFolder)
    filenamesLIST = glob.glob(POStaggedFolder + "/*.txt")
    #print(filenamesLIST)
    
    # Open evey tagged files
    for fileN_STR in filenamesLIST[:3]:
        with open (fileN_STR, errors="ignore", encoding="utf-8") as fileTXT:  # Use all "wlp-" tagged txt files, it contains POS taggings
            rawLIST = fileTXT.read().split("\n")  #.replace("\t", " ")
            rawLIST.pop(0) # remove the 1st and the 2nd elements in the LIST
            rawLIST.pop(0) # and the 2nd elements in the LIST
            pprint(rawLIST[:10])
            #print(type(rawLIST))
            #print(len(rawLIST))
        print("ORI_", len(rawLIST))
        
        # Remove the segment line in the raw txt file
        cleanedLIST = []
        for rowSTR in rawLIST:
            if "---" in rowSTR:
                #print(rowSTR)
                rawLIST.remove(rowSTR)
            else:
                pass
        print("NEW_", len(rawLIST))

        # Exclude the space in the string, and split them into a collected LIST
        for n_rowSTR in rawLIST:
            de_rowLIST = re.findall(r'\S+', n_rowSTR)  # [\s] = find space  ; \d+\s\d+ = find all set of (two strings of digits with " one" space in between); de = denoised strings
            #print("de_rowLIST", de_rowLIST)
            cleanedLIST.append(de_rowLIST)
        print(len(cleanedLIST))
                
