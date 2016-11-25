import sys
import os
from random import shuffle
import copy
import time

print (time.strftime("%H:%M:%S"))
distictDictionary=dict();
distictDictionaryAverage=dict();
fileAll=[]
fileDict=dict();
#o1 = open('per_model.txt','w', encoding="latin1")
count=1
#print(folderName)
hamfilelist=[]
spamfilelist=[]
o = open(os.path.dirname(os.path.abspath(sys.argv[0])) + "/per_model.txt", "w", 1, 'latin-1')
for dirname, dirnames, filenames in os.walk(str(sys.argv[1])):
    for subdirname in dirnames:
#         print(subdirname)
        if("ham" in str(subdirname)):
            for dirnameHam, dirnamesHam, filenamesHam in os.walk(os.path.join(dirname, subdirname)):
                for filenameHam in filenamesHam:
                    if(".txt" in filenameHam):
                        hamfilelist.append(os.path.join(os.path.join(dirname, subdirname), filenameHam))
#                 print("HamFileList size : " + str(len(hamfilelist)))
                        
        if("spam" in subdirname):
            for dirnameSpam, dirnamesSpam, filenamesSpam in os.walk(os.path.join(dirname, subdirname)):
                for filenameSpam in filenamesSpam:
                    if(".txt" in filenameSpam):
                        spamfilelist.append(os.path.join(os.path.join(dirname, subdirname), filenameSpam))
fileAll=spamfilelist+hamfilelist
#print (fileAll)
#print(len(fileAll))
fileAllCopy=fileAll
for f in fileAll:
    file1=open(f, "r", encoding="latin1")
    wordOfFiles=file1.read().split()
    #print(wordOfSpamFiles)
    fileDict[f]=wordOfFiles    
    for wordInDictionary in wordOfFiles:
        #if wordInDictionary not in distictDictionary:
        distictDictionary[wordInDictionary]=0
        distictDictionaryAverage[wordInDictionary]=0   

i=0
biasValue=0
betaValue=0
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


fileAllCopy=copy.deepcopy(fileAll)
for i in range(0,30):
    
    #print(i)
    #cc=0;
    #print(len(fileAllCopy))
    #print(len(fileAll))
    #alphaValue=0
    shuffle(fileAllCopy)    
    for i in range(0,len(fileAllCopy)): 
        f=fileAllCopy[i] 
        
        
        #earnFilePath = tempAllFileList[i]
    #     print("Learning file " + learnFilePath + " ")
        if(".ham.txt" in f):
    #             learnHamFile(learnFilePath)
            biasValue, count, betaValue = learnFile(f, hamY, biasValue, count, betaValue)
        elif (".spam.txt" in f):
    #             learnSpamFile(learnFile)
            biasValue, count, betaValue = learnFile(f, spamY, biasValue, count, betaValue)  
    #while fileAllCopy:
        #print(len(fileAllCopy))
        #f=random.choice(fileAllCopy)
        #print(f)
        #alphaValue=0
        #if ".spam.txt" in f:
        #    yValue=1
        #else:
        #    yValue=-1 
        #cc=cc+1
        #print(str(f)+" value of y is "+str(yValue))
        #file1=open(f, "r", encoding="latin1")
        #wordOfFiles=file1.read().split()
        #file1.close()
        #print(wordOfSpamFiles)
        #for wordInDictionary in wordOfFiles:
            #wordWeight=distictDictionary.get(wordInDictionary)
        #    alphaValue+=distictDictionary[wordInDictionary]
        #alphaValue+=biasValue
        #if(yValue*alphaValue<=0):
        #    for wordInDictionary in wordOfFiles:
        #        #wordWeight=distictDictionary.get(wordInDictionary)+yValue
        #        #wordWeight+=yValue
        #        distictDictionary[wordInDictionary]+=yValue
                #wordWeightAvg=distictDictionaryAverage.get(wordInDictionary)+(yValue*count)
                #wordWeightAvg+=yValue
        #        distictDictionaryAverage[wordInDictionary]+=(yValue*count)
                #distictDictionaryAverage.get(wordInDictionary)+distictDictionary.get(wordInDictionary)+
        #    biasValue+=yValue;
            #for wordInDictionary1 in wordOfFiles:
            #    wordWeightAvg=distictDictionaryAverage.get(wordInDictionary1)
            #    wordWeightAvg+=yValue
            #    distictDictionaryAverage[wordInDictionary1]=wordWeightAvg
        #    betaValue+=(yValue*count)
        #count=count+1
        #fileAllCopy.remove(f)
    #print(cc)
##print (betaValue)
#print(biasValue)
#print(count)
betaValue=biasValue-((1/count)*betaValue)
for wordInDictionary1 in distictDictionaryAverage:
    distictDictionaryAverage[wordInDictionary1] = distictDictionary[wordInDictionary1] - ((1/count)*distictDictionaryAverage[wordInDictionary1])
    
#print (betaValue)      

o.write("Value "+str(betaValue)+'\n')
#o1.write('\n')
for k in distictDictionaryAverage:
    #weight=distictDictionaryAverage.get(k)
    #res=k+" "+str(distictDictionaryAverage.get(k))
    o.write(k+" "+str(distictDictionaryAverage[k])+'\n')
    #o1.write('\n')
print (time.strftime("%H:%M:%S"))
o.close()
                