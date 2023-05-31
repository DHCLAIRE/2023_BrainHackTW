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
    print(filenamesLIST)
    
    # Open evey tagged files
    for fileN_STR in filenamesLIST:
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

        # Preporcess the tagged txt
        for n_rowSTR in rawLIST:
            #Exclude the space in the string, and split them into a collected LIST
            de_rowLIST = re.findall(r'\S+', n_rowSTR)  # [\s] = find space  ; \d+\s\d+ = find all set of (two strings of digits with " one" space in between); de = denoised strings
            
            #Delete the redundant POS tags
            if len(de_rowLIST) > 5:
                # Delete the possible POS tag
                del de_rowLIST[5:]
            else:
                pass
            """
            # find all puncs but no digits or word in it, and replace the original POS tag into "y" (same as COCA)
            if re.findall(r'[,|;|.|?|!|:]', de_rowLIST[2]) and not re.findall(r'[\w]', de_rowLIST[2]):
                de_rowLIST[-1] = de_rowLIST[-1].replace(de_rowLIST[-1], "y")
            else:
                pass
            """
            # Rename the most possible POS tags of the left POS
            if re.findall(r'[\w]+', de_rowLIST[-1]):  # [\w]+ = fina all seq without non-digits/chars at the end
                segPOS_LIST = re.findall(r'[\w]+', de_rowLIST[-1])
                de_rowLIST[-1] = segPOS_LIST[0]
            else:
                pass
            
            #switch the POS tag into lowercase(same as the COCA corpus)
            de_rowLIST[-1] = de_rowLIST[-1].lower()
            de_rowLIST.pop(3)
            if re.findall(r'[,|;|.|?|!|:|\W]', de_rowLIST[2]) and not re.findall(r'[\w]', de_rowLIST[2]):
                pass
            else:
                cleanedLIST.append(de_rowLIST)
            print("New___", de_rowLIST, len(de_rowLIST))
        print(len(cleanedLIST))
        pprint(cleanedLIST)
        
        # Save the cleaned POS tags into json file
        sub_idLIST = re.findall(r'S\d+_', fileN_STR)
        #print(sub_idLIST, type(sub_idLIST), sub_idLIST[0])
        with open(txtRoot_DIR_STR+'{}dePOS_LIST.json'.format(sub_idLIST[0]), "w", newline='', encoding="UTF-8") as jsonfile:
            json.dump(cleanedLIST, jsonfile, ensure_ascii=False)