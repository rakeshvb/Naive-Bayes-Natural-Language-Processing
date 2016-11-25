import sys
import os
from random import shuffle
import copy
import time

print (time.strftime("%H:%M:%S"))
distictDictionary=dict();
fileAll=[]
o = open('per_model.txt','w', encoding="latin1")
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):    
    for fn in filenames:
        if ".txt" in fn:
            fileAll.append(os.path.join(dirpath,fn))
fileAllCopy=fileAll
for f in fileAll:
    file1=open(f, "r", encoding="latin1")
    wordOfFiles=file1.read().split()    
    for wordInDictionary in wordOfFiles:
        #if wordInDictionary not in distictDictionary:
        distictDictionary[wordInDictionary]=0
i=0
biasValue=0
fileAllCopy=copy.deepcopy(fileAll) 
hamY = -1
spamY = 1

def learnFile(filePath, y, biasValue, count, betaValue):
#     print("read from " + filePath)
    #f1 = open(filePath, "r", encoding="latin1")
    #fileVocabList=f1.read().split()
    #f1.close()
    fileVocabList=fileDict[filePath]
    alphaValue = 0
    for word in fileVocabList:
        alphaValue += distictDictionary[word]
    alphaValue += biasValue
    
    if(y * alphaValue <= 0):
        for word in fileVocabList:
            distictDictionary[word] += y
            distictDictionaryAverage[word] += (y * count)
        biasValue += y
        betaValue += (y * count)
    count += 1
    return biasValue, count, betaValue

for i in range(0,20):    
    #print(i)
    #fileAllCopy=copy.deepcopy(fileAll)    
    shuffle(fileAllCopy)    
    for f in fileAllCopy:    
        alphaValue=0
        if "spam.txt" in f:
            yValue=1
        else:
            yValue=-1         
        file1=open(f, "r", encoding="latin1")
        wordOfFiles=file1.read().split()
        for wordInDictionary in wordOfFiles:
            alphaValue+=distictDictionary.get(wordInDictionary)
        alphaValue+=biasValue
        if(yValue*alphaValue<=0):
            for wordInDictionary in wordOfFiles:
                #wordWeight=distictDictionary.get(wordInDictionary)+yValue
                #wordWeight+=yValue
                distictDictionary[wordInDictionary]=distictDictionary.get(wordInDictionary)+yValue
            biasValue+=yValue;        
#r="BiasValue "+str(biasValue)
o.write("Value "+str(biasValue)+'\n')
#o.write('\n')
for k in distictDictionary.keys():
    #weight=distictDictionary.get(k)
    #res=k+" "+str(distictDictionary.get(k))
    o.write(str(k)+" "+str(distictDictionary.get(k))+'\n')
    #o.write('\n')
print (time.strftime("%H:%M:%S"))
o.close()
                