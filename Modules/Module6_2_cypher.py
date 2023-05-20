#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import re
import argparse

# Import the self-defined func from self-made script
from Module6_1_useful_functions import process_message

def main(input_path, keySTR, mode, output_path):
    '''
    To decypher the messge, and save it into a file
    *input_path*: the path of the messege
    *keySTR*: the key in string form
    *mode*: To encrypt or decrypt
    *output_path*: the output file path (=where to save it)
    '''
    
    # Open and then read the messege file according to its path
    with open(input_path, "r", encoding="utf-8") as messege_file:
        messegeSTR = messege_file.read()
    '''one-liner NOTE
    one-liner =>> messege_fileSTR = open(messege_path, "r", encoding="utf-8")
    one-liner will need to add => messege_fileSTR.close() after it.
    However, if anything error in the one-liner which led the .close() did not perform
    , then any changes happended to the file would stay permernent.
    '''
    # set the mode as encryption
    encryptMODE = mode =="encryption"
    # process the messege by the self-defined func
    processed_messegeSTR = process_message(messegeSTR, keySTR, encryptMODE)
    #open a new file to save the processed messeges
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(processed_messegeSTR)
        

if __name__ == "__main__":
    # Create the argument parser by functions in argparse(python module)
    arg_parserFUNC = argparse.ArgumentParser()
    # For input file argument
    arg_parserFUNC.add_argument("-i", dest="input_path", type=str, required=True, help="The input path of the file.")
    # For input file argument
    arg_parserFUNC.add_argument("-o", dest="output_path", type=str, required=True, help="The output path of the file.")
    # For keySTR argument
    arg_parserFUNC.add_argument("-k", dest="keySTR", type=str, required=True, help="The keySTR for the messege.")
    # For the "mode" argument (An additional option for choices)
    arg_parserFUNC.add_argument("-m", dest="mode", type=str, required=True, choices=["encryption", "decryption"], help="To encrypt or decrypt the messege.")
    
    # To set the arguments' position??
    args = arg_parserFUNC.parse_args()
    main(args.input_path, args.keySTR, args.mode, args.output_path)
