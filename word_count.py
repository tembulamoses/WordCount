#!/usr/bin/env python
# -*- coding: utf-8 -*- 
def words(sentence):
    """A function that takes a string as an argument, and returns a dictionary
    containing the words in the dictionary as key with the number of times they
     appear as the values.
     For example for the input "olly, olly. in come-free". it produces
     { olly: 2, in: 1, come: 1, free: 1 }
     
    NOTED: for now, this function is not fully optimized but atleased it passes the basic tests in here
     eg if we had a float, it should be noted as one word and so on. Some of the real life experiences were not noted thus this program has some reservations for the same
     """
    #The sentence is first split into wotds using spaces only
    words= sentence.split()
    """We have delimiters around whiich a word is counted as a word buut they are not counted as words. They include fullstops, commas and hyphens which are removed from words that were next
    to them in the sentences"""
    for delimiter in ["."," " '\n', '\t']:
        # The removal of the delimiters
        words = [word.split(delimiter)[0] for word in words]
        
    
    """Python has the tendency to identify the variables by what they are eg an integer is noted as so and not as string , thus for the boundaries of these tests, just the integers and strings"""    

    #The occurance of the words in the sentences are then counted
    dictionary = { word:words.count(word) for word in words if not word.isdigit()}
    
    #counting the digits too
    dictionary.update({ int(word):words.count(word) for word in words if word.isdigit()})

    return dictionary