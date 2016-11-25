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


fileAllCopy=copy.deepcopy(fileAll)
for i in range(0,30):
    
    
    shuffle(fileAllCopy)    
    for i in range(0,len(fileAllCopy)): 
        f=fileAllCopy[i] 
     
        alphaValue=0
        if ".spam.txt" in f:
            yValue=1
        else:
            yValue=-1 
        wordOfFiles=fileDict[f]
        
        for wordInDictionary in wordOfFiles:
            #wordWeight=distictDictionary.get(wordInDictionary)
            alphaValue+=distictDictionary[wordInDictionary]
        alphaValue+=biasValue
        if(yValue*alphaValue<=0):
            for wordInDictionary in wordOfFiles:
 
                distictDictionary[wordInDictionary]+=yValue
  
                distictDictionaryAverage[wordInDictionary]+=(yValue*count)

            biasValue+=yValue;
           
            betaValue+=(yValue*count)
        count=count+1
        
betaValue=biasValue-((1/count)*betaValue)
for wordInDictionary1 in distictDictionaryAverage:
    distictDictionaryAverage[wordInDictionary1] = distictDictionary[wordInDictionary1] - ((1/count)*distictDictionaryAverage[wordInDictionary1])
o.write("Value "+str(betaValue)+'\n')

for k in distictDictionaryAverage:

    o.write(k+" "+str(distictDictionaryAverage[k])+'\n')
    #o1.write('\n')
print (time.strftime("%H:%M:%S"))
o.close()
                