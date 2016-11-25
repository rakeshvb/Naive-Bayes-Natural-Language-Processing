import sys
import os
import random
import copy

distictDictionary=dict();
fileAll=[]
fileAllCopy=fileAll
o = open('per_model.txt','w', encoding="latin1")
#print(folderName)
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    #print (dirpath, dirnames, filenames)
    for fn in filenames:
        if ".txt" in fn:
            fileAll.append(os.path.join(dirpath,fn))
#print (fileAll)
#print(len(fileAll))

for f in fileAll:
    file1=open(f, "r", encoding="latin1")
    wordOfFiles=file1.read().replace('\n',' ').split()
    #print(wordOfSpamFiles)
    for wordInDictionary in wordOfFiles:
        if wordInDictionary not in distictDictionary:
            distictDictionary[wordInDictionary]=0
        #else:
        #    distictDictionary[wordInDictionary]=0
#print(distictDictionary)
#print(len(distictDictionary.keys()))  

i=0
biasValue=0
for i in range(0,20):
    fileAllCopy=copy.deepcopy(fileAll)
    print(i)
    cc=0;
    #print(len(fileAllCopy))
    #print(len(fileAll))
    #alphaValue=0
    while fileAllCopy:
        #print(len(fileAllCopy))
        f=random.choice(fileAllCopy)
        #print(f)
        alphaValue=0
        if "spam.txt" in f:
            yValue=1
        else:
            yValue=-1 
        cc=cc+1
        #print(str(f)+" value of y is "+str(yValue))
        file1=open(f, "r", encoding="latin1")
        wordOfFiles=file1.read().replace('\n',' ').split()
        #print(wordOfSpamFiles)
        for wordInDictionary in wordOfFiles:
            #wordWeight=distictDictionary.get(wordInDictionary)
            alphaValue+=distictDictionary.get(wordInDictionary)
        alphaValue+=biasValue
        if(yValue*alphaValue<=0):
            for wordInDictionary in wordOfFiles:
                wordWeight=distictDictionary.get(wordInDictionary)
                wordWeight+=yValue
                distictDictionary[wordInDictionary]=wordWeight
            biasValue+=yValue;
        fileAllCopy.remove(f)
    print(cc)
      
#print(distictDictionary) 
#print(biasValue) 
#print(len(distictDictionary))
r="BiasValue "+str(biasValue)
o.write(r)
o.write('\n')
for k in distictDictionary.keys():
    #weight=distictDictionary.get(k)
    res=k+" "+str(distictDictionary.get(k))
    o.write(res)
    o.write('\n')
o.close()
                