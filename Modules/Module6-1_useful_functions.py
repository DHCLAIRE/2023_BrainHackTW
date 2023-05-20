#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import csv
import json
import random
from random import sample
import os
from gtts import gTTS
import pandas as pd
import time
from pathlib import Path
import nltk
import re
import argparse
#from nltk import sent_tokenize
#from nltk import tokenize

def encrypt_message(letterSTR, keySTR):
    '''
    To encryt the messege by using the key (in unicode form)
    , hence return a new representation as the result. 
    e.g. messege = "l"; key = "h"; return = "Ô"
    '''
    letterSTR_indexINT = ord(letterSTR)
    keySTR_indexINT = ord(keySTR)
    # get the encrypted (result) index by get the residue of (letterSTR_indexINT + keySTR_indexINT) / 1114112
    encrypted_indexINT = (letterSTR_indexINT + keySTR_indexINT) % 1114112  
    
    return chr(encrypted_indexINT) # characterize the result from its unicode sequence

def decrypt_message(letterSTR, keySTR):
    '''
    To decryt the messege by using the key (in unicode form)
    , hence return a new representation as the result. 
    e.g. key = "h"; messege = "l"; return = "Ô"
    '''
    letterSTR_indexINT = ord(letterSTR)
    keySTR_indexINT = ord(keySTR)
    # get the encrypted (result) index by get the residue of (letterSTR_indexINT - keySTR_indexINT) / 1114112  # Why minus??
    decrypted_indexINT = (letterSTR_indexINT - keySTR_indexINT) % 1114112
    
    return chr(decrypted_indexINT) # characterize the result from its unicode sequence

def process_message(messageSTR, keySTR, encryptionBOOL):
    '''
    To process the target messege and verify the encryption correctness
    , hence return a conformation strings to answer the test acomplishment.  ??
    e.g. messege = "l"; key = "h"; return = "Ô", encryptionBOOL = True   >>??
    '''
    processed_messageSTR = ""
    
    if encryptionBOOL == True:
        message_processFUNC = encrypt_message #(letterSTR, keySTR)
    else:
        message_processFUNC = decrypt_message #(letterSTR, keySTR)  # correct??
    
    for indexINT, letterSTR in enumerate(messageSTR):
        key_letterSTR = keySTR[indexINT %len(keySTR)]  #double check this concept in case I got confused
        processed_keySTR = message_processFUNC(letterSTR, key_letterSTR)
        processed_messageSTR += processed_keySTR
    return processed_messageSTR


if __name__ == "__main__":
    testSTR = encrypt_message("k", "o")
    print(testSTR)  # Is it like to use whatever key to produce/protext the message?
    
    test_letterSTR = "k"
    test_keySTR = "o"
    
    decrypted_messageSTR = decrypt_message(encrypt_message(test_letterSTR, test_keySTR), test_keySTR)
    
    if test_letterSTR == decrypted_messageSTR:
        print("1st function check SUCCEED.")
    else:
        print("1st function check FAIL.")
        
    test_messageSTR = "message"
    test_keySTR = "key"
    
    encrypted_messageSTR = process_message(test_messageSTR, test_keySTR, encryptionBOOL=True)
    decrypted_messageSTR = process_message(encrypted_messageSTR, test_keySTR, encryptionBOOL=False)
    
    if decrypted_messageSTR == test_messageSTR:
        print("2nd function check SUCCEED.")
    else:
        print("2nd function check FAILED.")