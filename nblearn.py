import sys
import os

file_spam=[]
file_not_spam=[]
hamDictionary=dict();
spamDictionary=dict();
probDictOfHamWords=dict();
probDictOfSpamWords=dict();
print("enter the path " +  str(sys.argv[1]))

for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    #print (dirpath, dirnames, filenames)
    for fn in filenames:
        if ".txt" in fn:
            if "spam" in fn:
                file_spam.append(os.path.join(dirpath,fn))
            else:
                 file_not_spam.append(os.path.join(dirpath,fn))
#print(file_spam)
#print(file_not_spam)
spamFileNumber=len(file_spam)
hamFileNumber=len(file_not_spam)
probOfSpamFiles=((spamFileNumber)/(spamFileNumber+hamFileNumber))
probOfhamFiles=((hamFileNumber)/(spamFileNumber+hamFileNumber))
print("SPAM Probability: "+ str(probOfSpamFiles))
print("HAM Probability: "+str(probOfhamFiles))


#Spam File Calculation

for spam in file_spam:
    file1=open(spam, "r", encoding="latin1")
    wordOfSpamFiles=file1.read().replace('\n',' ').split(' ')
    #print(wordOfSpamFiles)
    for spamDistinctWords in wordOfSpamFiles:
        if spamDistinctWords in spamDictionary:
            num=spamDictionary.get(spamDistinctWords)
            spamDictionary[spamDistinctWords]=num+1
        else:
            spamDictionary[spamDistinctWords]=1
            
spamDictionary.pop('')
#print(spamDictionary)
distNumberOfWordsInSpamFiles=len(spamDictionary.keys())
print(distNumberOfWordsInSpamFiles)  


###Spam File Word Probability Count

allWordCountInSpam=0
for j in spamDictionary.keys():
    allWordCountInSpam+=spamDictionary[j]

for asd in spamDictionary.keys():
    count=spamDictionary[asd]
    prob_asd=count/allWordCountInSpam
    probDictOfSpamWords[asd]=prob_asd     

print(probDictOfSpamWords)

#Non-Spam File Calculation

for ham in file_not_spam:
    file2=open(ham, "r", encoding="latin1")
    wordOfHamFiles=file2.read().replace('\n',' ').split(' ')
    #print(wordOfSpamFiles)
    for hamDistinctWords in wordOfHamFiles:
        if hamDistinctWords in hamDictionary:
            num2=hamDictionary.get(hamDistinctWords)
            hamDictionary[hamDistinctWords]=num2+1
        else:
            hamDictionary[hamDistinctWords]=1

hamDictionary.pop('')            
#print(hamDictionary)
distNumberOfWordsInHamFiles=len(hamDictionary.keys())
print(distNumberOfWordsInHamFiles)          

###Hpam File Word Probability Count
allWordCountInHam=0
for i in hamDictionary.keys():
    allWordCountInHam+=hamDictionary[i]


for asd1 in hamDictionary.keys():
    count1=hamDictionary[asd1]
    prob_asd1=count1/allWordCountInHam
    probDictOfHamWords[asd1]=prob_asd1          
print(probDictOfHamWords)
        
    
    
    
