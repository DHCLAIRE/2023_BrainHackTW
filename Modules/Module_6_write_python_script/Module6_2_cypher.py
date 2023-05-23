#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import re
import argparse

# Import the self-defined func from self-made script
from Module6_1_useful_functions import process_message

def main(input_path, keySTR, mode):
    '''
    To decypher the messge, and save it into a file
    *input_path*: the path of the messege
    *keySTR*: the key in string form
    *mode*: To encrypt or decrypt
    #*output_path*: the output file path (=where to save it)  =>> correction: include in the function but not in arg
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
    # Check the bool condition of the mode (as encryption or not>> TRUE/FALSE)
    encryptBOOL = mode =="enc"  ##=>> correction: "encryption" to "enc"
    # process the messege by the self-defined func
    processed_messegeSTR = process_message(messegeSTR, keySTR, encryptBOOL)
    #open a new file to save the processed messeges
    if mode == "enc":
        if "decrypted" in input_path:
            output_filenameSTR = input_path[:-14]  # exclude the "decrypted.txt" str
            txt_suffix = "_encrypted"
        else:
            output_filenameSTR = input_path[:-4]  # exclude the ".txt" str
            txt_suffix = "_encrypted"
    else:
        if "encrypted" in input_path:
            output_filenameSTR = input_path[:-14]  # exclude the "decrypted.txt" str
            txt_suffix = "_decrypted"
        else:
            output_filenameSTR = input_path[:-4]  # exclude the ".txt" str
            txt_suffix = "_decrypted"
    with open("%s%s.txt"%(output_filenameSTR, txt_suffix), "w", encoding="utf-8") as output_file:
        output_file.write(processed_messegeSTR)
        

if __name__ == "__main__":
    # Create the argument parser by functions in argparse(python module)
    arg_parserFUNC = argparse.ArgumentParser()
    # For input file argument
    arg_parserFUNC.add_argument("--message", dest="input_path", type=str, required=True, help="The input path of the file.")
    # For input file argument
    #arg_parserFUNC.add_argument("-o", dest="output_path", type=str, required=True, help="The output path of the file.")
    # For keySTR argument
    arg_parserFUNC.add_argument("--key", dest="keySTR", type=str, required=True, help="The keySTR for the messege.")
    # For the "mode" argument (An additional option for choices)
    arg_parserFUNC.add_argument("--mode", dest="mode", type=str, required=True, choices=["enc", "dec"], help="To encrypt or decrypt the messege.")
    
    # To set the arguments' position??
    args = arg_parserFUNC.parse_args()
    main(args.input_path, args.keySTR, args.mode) # =>> correction: delete args.output_path
    print("DONE.")
