#import xlrd
#import pandas as pd

def getShorter(string1, string2):
    if len(string1) > len(string2):
        return string2
    return string1


###----- Getting the data about crops in Trinidad -----###
from xlrd import open_workbook

count=0
produce_list={}
col_value = []
wb = open_workbook('testdata.xls')
for s in wb.sheets():
    #print 'Sheet:',s.name
    
    for row in range(s.nrows):
        count=0
        col_value = []
        for col in range(s.ncols):
            count+=1
            if count==1:
                val=""
                value  = (s.cell(row,col).value)
                try : value = str(int(value))
                except : pass
                for i in range(len(value)):
                    if value[i]=='(':
                        break
                    val+=value[i]
                dictID=val.lower()
                #print(dictID)
            if count==2:
                value  = (s.cell(row,col).value)
                try : value = str(int(value))
                except : pass
                col_value.append(value)
            if count==7:
                value  = (s.cell(row,col).value)
                try : value = str(int(value))
                except : pass
                col_value.append(value)
        produce_list[dictID]=col_value
        #values.append(col_value)
        
        
######----Scraping Nutritional Data From Online----######
import requests as rq
from bs4 import BeautifulSoup

for i in produce_list:
    print(i)
    
requestOne = rq.get("http://www.myfitnesspal.com/food/search")#Scraping data from the entire online database
contentOne = requestOne.content #Storing the entire html file in a string
soup = BeautifulSoup(contentOne, "html.parser")

#Scraping nutritional data on banana


#for td in bananaSoup.find(text='Potassium').parent.find_next_siblings():
#    print(td.text)
    


#print([str(tag.text) for tag in soup.find_all("a")])


#element = soup.find("a", text = 'Doubles W/ Channa') #getting the a element with the href specified
#print(soup.prettify() + "tevin")
#print(element['href'])
    
    
import requests
import unicodedata
#from bs4 import BeautifulSoup

itemData = {}
#Format : "Vegetable" : [Sodium, Potassium, Dietary Fiber, Sugars, Protein]
itemData["tevin"] = [3, 2, 3, 3, 5]
classList = []
#Doing a Google Search for each item to scrape the nutritional data
for item in produce_list:
    query = item + " myfitnesspal" #googling each food item in the Trinidad produce list
    google_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + query
    
    
    r = requests.get(google_search)
    
    soupT = BeautifulSoup(r.text, "html.parser") 
    link =  soupT.find('cite').text
    link = unicodedata.normalize('NFKD', link).encode('ascii', 'ignore') #Converting unicode link to String
    
    
    
    if "www.myfitnesspal.com" in link:
        #if "tag" in link or "nutrition" in link:
            #print("The {} link returns a search page".format(item))
            #print(link)
            
            
        if "..." in link:
            if "food" in link:
                link = link.replace("...", "categories")
                
                itemRequest = rq.get("http://" + link)
                itemContent = itemRequest.content
                
                
                if "Member Login" in itemContent:
                    link = link.replace("categories", "calories") 
                
                itemRequest = rq.get("http://" + link)
                itemContent = itemRequest.content
                itemSoup = BeautifulSoup(itemContent, "html.parser")
                #print(item)
                #print(link)
        else:
            itemRequest = rq.get("http://" + link)
            itemContent = itemRequest.content
            itemSoup = BeautifulSoup(itemContent, "html.parser")
        
        
        
        #print(itemSoup.prettify())
        allNutrName = itemSoup.findAll('td', { 'class' : 'col-1' }) #Stores the title of all nutrients
        
        if not allNutrName is None and not len(allNutrName) == 0:
            calName = allNutrName[0]
            sugName = allNutrName[1]
            cholName = allNutrName[2]
            vitAName = allNutrName[3]
            vitCName = allNutrName[4]
            
            allNutr = itemSoup.findAll('td', { 'class' : 'col-2' }) #Stores the values of all nutrients
            
            if not allNutr is None and not len(allNutr) == 0:
                calVal = allNutr[0].text
                sugVal = allNutr[1].text
                cholVal = allNutr[2].text
                vitAVal = allNutr[3].text
                vitCVal = allNutr[4].text
        
        #if not allNutr is None and not allNutrName is None:
                itemData[item] = [calVal, sugVal, cholVal, vitAVal, vitCVal]  


print(itemData["carrot"])
print(itemData["christophene"])
        
#bananaRequest = rq.get("http://www.myfitnesspal.com/food/calories/543987619")#Getting the nutritional data for bananas
#bananaContent = bananaRequest.content
#bananaSoup = BeautifulSoup(bananaContent, "html.parser")
#print(bananaSoup.prettify())
#bananaDetails = {}
#bananaPotassium = bananaSoup.find("td", text = 'Potassium')
        
    
    
