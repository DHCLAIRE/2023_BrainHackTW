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
            pprint(rawLIST[:10])
            print(type(rawLIST))
            print(len(rawLIST))
            for row in rawLIST:
                print(row)
                print(type(row))
                print(len(row))