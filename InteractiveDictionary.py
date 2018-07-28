# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:27:38 2018

@author: admin
"""

import json
from difflib import get_close_matches
data=json.load(open("data.json"))
print("\n      "+ "  THANK YOU FOR SELECTING INTERACTIVE LIBRARY!!!")
isExit="y"
newdata={k.lower(): v for k, v in data.items()}

def findMeaning(w):        
        if w in newdata.keys():
            return newdata[w] 
        elif len(get_close_matches(w,newdata.keys()))>0:
            isMatch=input("Did you mean %s ? \n  Enter (y/n): " % get_close_matches(w,newdata.keys())[0])
            if isMatch=="y":
                return newdata[get_close_matches(w,newdata.keys())[0]]
            elif isMatch=="n":
                return "\nThen sorry!!! We don't have anything..:("
            else:
                return "\nWe didn't get you...:|"
        else:
            return"\nSorry!!! Meaning not found..:("
 
while isExit=="y" :
    word=input("Enter the word to know meaning:").lower()
    result=findMeaning(word)
    if type(result) ==list:
        print("Hey !! you're lucky..Here is your meaning..")
        for meaning in result:
            print(meaning+"\n")
    else:
        print(result)
   
        
    isExit=input("Want to continue(y/n):")
    if isExit=="y":
        continue
    elif isExit=="n":
        print("\nThank you for using Interactive Library...:)")
    else:
        print("\nInvalid Input...Thank you..!!!")
        
