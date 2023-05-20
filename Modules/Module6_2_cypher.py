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

# Import the self-defined func from self-made script
from Module6_1_useful_functions import process_message

def main(messege_path, keySTR, mode):
    '''
    To decypher the messge, and save it into a file
    *messege_path*: the path of the messege
    *keySTR*: the key in string form
    *mode*: To encrypt or decrypt
    *output_path*: the output file path (=where to save it)
    '''
    with open(messege_path, "r", encoding="utf-8") as messegeSTR:


if __name__ == "__main__":