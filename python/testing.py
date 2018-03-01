# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:37:56 2018

@author: 816000026
"""

def toLowerCase(value):
    """
    Converting a string to lower case
    """
    
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    newString = ""
    
    for i in range(len(value)):
        if value[i] in upper_alphabet:
            newString += lower_alphabet[upper_alphabet.index(value[i])]
        if value[i] in lower_alphabet:
            newString += value[i]
    
    return newString






import requests as rq
from bs4 import BeautifulSoup




#nutrient = raw_input("which nutrient: ")
#print(toLowerCase(nutrient))


#if toLowerCase(nutrient) == "protein":
#    extension = "/foods_by_Protein_content.html"
#if toLowerCase(nutrient) == "carbohydrate":
#    extension = "/foods_by_Carbohydrate_content.html"
#if toLowerCase(nutrient) == "fiber":
#    extension = "/foods_by_Fiber_content.html"

    
    
request = rq.get("https://ndb.nal.usda.gov")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("a", {'href' : '/foods_by_Protein_content.html'}) #getting the a element with the href specified
print(request.content)

#print(element.text)
#Protein
#https://www.nutritionvalue.org/foods_by_Fiber_content.html
