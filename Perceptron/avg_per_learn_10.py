import sys
import os
from random import shuffle
import copy
import time

print (time.strftime("%H:%M:%S"))
distictDictionary=dict();
fileDict=dict();
fileAll=[]
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
fileAllCopy=fileAll
  
for f in fileAll:
    file1=open(f, "r", encoding="latin1")
    wordOfFiles=file1.read().split()
    fileDict[f]=wordOfFiles    
    for wordInDictionary in wordOfFiles:
        #if wordInDictionary not in distictDictionary:
        distictDictionary[wordInDictionary]=0
i=0
biasValue=0

hamY = -1
spamY = 1
def learnFile(filePath, y, bias):
#     print("read from " + filePath)
    #f1 = open(filePath, "r", encoding="latin1")
    #fileVocabList=f1.read().split()
    #f1.close()
    fileVocabList=fileDict[filePath]
    alphaValue = 0
    for word in fileVocabList:
        alphaValue += distictDictionary[word]
    alphaValue += bias
    
    if(y * alphaValue <= 0):
        for word in fileVocabList:
            distictDictionary[word] += y
        bias += y
    return bias

fileAllCopy=copy.deepcopy(fileAll) 
for i in range(0,20):    
    #print(i)
    #fileAllCopy=copy.deepcopy(fileAll)    
    shuffle(fileAllCopy)    
    for i in range(0,len(fileAllCopy)): 
        f=fileAllCopy[i]   
        alphaValue=0
        if(".ham.txt" in f):
    #             learnHamFile(learnFilePath)
            biasValue = learnFile(f, hamY, biasValue)
        elif (".spam.txt" in f):
    #             learnSpamFile(learnFile)
            biasValue = learnFile(f, spamY, biasValue)
        #if "spam.txt" in f:
        #    yValue=1
        #else:
        #    yValue=-1         
        #file1=open(f, "r", encoding="latin1")
        #wordOfFiles=file1.read().split()
        #for wordInDictionary in wordOfFiles:
        #    alphaValue+=distictDictionary.get(wordInDictionary)
        #alphaValue+=biasValue
        #if(yValue*alphaValue<=0):
        #    for wordInDictionary in wordOfFiles:
        #        #wordWeight=distictDictionary.get(wordInDictionary)+yValue
        #        #wordWeight+=yValue
        #        distictDictionary[wordInDictionary]=distictDictionary.get(wordInDictionary)+yValue
        #    biasValue+=yValue;        
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
                