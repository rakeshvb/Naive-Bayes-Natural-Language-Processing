import sys
import os
from random import shuffle
import copy
import time

print (time.strftime("%H:%M:%S"))
distictDictionary=dict();
fileDict=dict()
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
file10=[]
l=len(fileAll)*(0.10)
hh=0
h=0
#fl=True
for f in fileAll:

    
    if "spam.txt" in f:
        if hh<l:
            file10.append(f)
            hh=hh+1
    else:
        if h<l:
            file10.append(f)
            h=h+1

fileAllCopy=file10
  
for f in file10:
    file1=open(f, "r", encoding="latin1")
    wordOfFiles=file1.read().split()
    fileDict[f]=wordOfFiles    
    for wordInDictionary in wordOfFiles:
        #if wordInDictionary not in distictDictionary:
        distictDictionary[wordInDictionary]=0
i=0
biasValue=0


fileAllCopy=copy.deepcopy(file10) 
for i in range(0,20):    
    #print(i)
    #fileAllCopy=copy.deepcopy(fileAll)    
    shuffle(fileAllCopy)    
    for i in range(0,len(fileAllCopy)): 
        f=fileAllCopy[i]   
        alphaValue=0

        if "spam.txt" in f:
            yValue=1
        else:
            yValue=-1   
        wordOfFiles=fileDict[f]      

        for wordInDictionary in wordOfFiles:
            alphaValue+=distictDictionary[wordInDictionary]
        alphaValue+=biasValue
        if(yValue*alphaValue<=0):
            for wordInDictionary in wordOfFiles:

                distictDictionary[wordInDictionary]+=yValue
            biasValue+=yValue;        
#r="BiasValue "+str(biasValue)
o.write("Value "+str(biasValue)+'\n')
#o.write('\n')
for k in distictDictionary.keys():
    
    o.write(str(k)+" "+str(distictDictionary.get(k))+'\n')
    
print (time.strftime("%H:%M:%S"))
o.close()
                