#!/usr/bin/python
import csvTest


def main():
    price = 0
    finalCrop = {}
    reallyFinalCrop = {}
    crops = csvTest.getXlData()
    array = []
    array2 = []
    nutrients = csvTest.getCrops()
    budget = input("Input the income of your household in the format $00.00: $")
    numPeop = input("Input the number of people in the household: ")
    #period = input("How do you want your budget based? Daily/Weekly/Bi-weekly/Monthly: ")

    #budgetPerPerson = float(budget)/int(numPeop)
    
    for crop in crops.items():
        #print(crop)
        if crop[1][1] != '' and crop[0]!="commodity":
            finalCrop[crop[0]] = crop[1]

    for keys in finalCrop.items():
        for crop in nutrients.items():
            if keys[0] in crop[0]:
                reallyFinalCrop[keys[0]] = crop[1] + keys[1]
    print(reallyFinalCrop)   
    #print("$",budget, numPeop, period)
    #sys.argv[]
    for prices in reallyFinalCrop.values():
        array.append(prices[6])

    for helpme in reallyFinalCrop.values():
        array2.append(helpme[0:4])
    #knapSack(budget, array, array2, len(reallyFinalCrop))
    
def knapSack(budget , prices , nutValue , n):  
    # Base Case
    if n == 0 or budget == 0 :# or nutvalue
        return 0
    if (prices[n-1] > budget):
        return knapSack(budget , prices , nutValue , n-1)
    else:
        #   val of second to last item
        
        return max((nutValue[n-1][0] + nutValue[n-1][1] + nutValue[n-1][2] + nutValue[n-1][3] + nutValue[n-1][4])  + knapSack(budget-prices[n-1] , prices , nutValue , n-1), knapSack(budget , prices , nutValue , n-1))

#print(knapSack(budget , prices , nutValue , n))



if __name__ == '__main__':
    main()
