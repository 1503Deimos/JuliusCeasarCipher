#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:07:12 2021

@author: 1503Deimos
"""

import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def main():
    keyword = input("\nEnter key word to create cipher alphabet: \n")
    index = int(input("Enter the number of spaces to offset the cipher alphabet: "))
    
    cipher_alphabet_no_duplicates = create_cipher_key(keyword, index, ALPHABET)
    final_key = create_ciph_dict(ALPHABET, cipher_alphabet_no_duplicates)
    for key, value in final_key.items():
        print(key, ' : ', value)
    plaintext_mesg = decrypt(final_key)   
    print(plaintext_mesg)
    
    
def create_cipher_key(keyword, index, alphabet):
    """Creates the substitution cipher alphabet string based on keyword and 
    spaces input"""
    alph_ind = int(26 - index)
    keyword = ''.join([j for i,j in enumerate(keyword) if j not in keyword[:i]])
    if len(keyword) > 26:
        print("Keyword is too long.  Please try again.", file= sys.stderr)
        sys.exit()
    print(keyword)

    cipher_alphabet = "".join(alphabet[alph_ind:] + keyword + alphabet[:-index])
    cipher_alphabet_no_duplicates = "".join([j for i,j in enumerate(cipher_alphabet) 
                                             if j not in cipher_alphabet[:i]]).upper()
    return cipher_alphabet_no_duplicates

def create_ciph_dict(alphabet, cipher_alphabet_no_duplicates):
    """Creates a dictinary for the plaintext alphabet and cipher final cipher 
    alphabet"""
    final_key = dict(zip(ALPHABET, cipher_alphabet_no_duplicates))
    return final_key

def decrypt(final_key):
    encryption_text = input("""
Enter the message you would like to decrypted with the Julius Ceasar Cipher:
""")
    plaintext_mesg = []
    encryption_text = list(encryption_text)
    print(encryption_text)
    for letter in encryption_text:
        for key, values in final_key.items():
            if letter == values:
                plaintext_mesg.append(key)
    plaintext_mesg = ''.join(plaintext_mesg)       
    return plaintext_mesg

if __name__ == '__main__':
    main()