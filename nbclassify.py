import sys
import os

print("enter the path " +  str(sys.argv[1]))
print("enter the second path " +  str(sys.argv[2]))


file_nbmodel=open(os.path.join(str(sys.argv[1]),"nbmodel.txt"),"r", encoding="latin-1")
nbmodel_read=[]
for word in file_nbmodel:
    nbmodel_read.append(word)

#print(nbmodel_read)
spamDictionary=dict()
hamDictionary=dict()
hamWordList=[]
spamWordList=[]
for i in range(0,len(nbmodel_read)):
    newline=nbmodel_read[i].split(' ')
    num=len(newline)
    if(num==2):
        if(i==0):
            Spam_Prob=float(newline[1])
        if(i==1):
            Non_Spam_Prob=float(newline[1])
        if(i==2):
            Dist_No_Of_WordsSpam=int(newline[1])
        if(i==3):
            Dist_No_Of_WordsHam=int(newline[1])
        if(i==4):
            Words_In_Spam_File=int(newline[1])
        if(i==5):
            Words_In_Ham_File=int(newline[1])
    elif(num==4):
        if "Spam " in nbmodel_read[i]:
            #print("hello")
            spamDictionary[newline[1]]=[float(newline[2]), float(newline[3])]
        if "Ham " in nbmodel_read[i]:
            hamDictionary[newline[1]]=[float(newline[2]), float(newline[3])]
#print(Spam_Prob)
#print(Non_Spam_Prob)
#print(Dist_No_Of_WordsSpam)
#print(Dist_No_Of_WordsHam)
#print(Words_In_Ham_File)
#print(Words_In_Spam_File)
#print(spamDictionary)
#print(hamDictionary)
c1=0
distNumberOfWordsInSpamFiles=len(spamDictionary.keys())
distNumberOfWordsInHamFiles=len(hamDictionary.keys())
#print(distNumberOfWordsInSpamFiles)
#print(distNumberOfWordsInHamFiles)
file=[]
for dirpath, dirnames, filenames in os.walk(sys.argv[2]):
    for fn in filenames:
        if ".txt" in fn:
            file.append(os.path.join(dirpath,fn))
#print(file)
classes=["Ham","Spam"]
#Dictionary filename:Label
resultDict=dict()
PredictDictionary=dict()
for ha in file:
    file1=open(ha, "r", encoding="latin1")
    wordOfFiles=file1.read().replace('\n',' ').split()
    #print(wordOfSpamFiles)
    spamProb=1.0
    hamProb=1.0
    for wor in wordOfFiles:
        if(wor in spamDictionary.keys()):
            spamProb*=spamDictionary[wor][1]
        if (wor not in spamDictionary.keys() and wor in hamDictionary):
            #add one smoothing
            spamProb=1/(Dist_No_Of_WordsHam+Dist_No_Of_WordsSpam+Dist_No_Of_WordsSpam)
        if(wor in hamDictionary.keys()):
            hamProb*=hamDictionary[wor][1]
        if(wor not in hamDictionary.keys() and wor in spamDictionary):
            #add one smoothing
            hamProb=1/(Dist_No_Of_WordsHam+Dist_No_Of_WordsHam+Dist_No_Of_WordsSpam)
        if(wor not in hamDictionary and wor not in spamDictionary):
            hamProb=1.0
            spamProb=1.0
    resultForSpam=((Spam_Prob*spamProb)/((Spam_Prob*spamProb)+(Non_Spam_Prob*hamProb)))
    resultForHam=((Non_Spam_Prob*hamProb)/((Spam_Prob*spamProb)+(Non_Spam_Prob*hamProb)))
    if resultForSpam>resultForHam:
        resultDict[ha]=classes[1]
    if resultForHam>resultForSpam:
        resultDict[ha]=classes[0]
    #print(resultDict)
print(resultDict)       
            


        
            
            
        
        
    

      

        
