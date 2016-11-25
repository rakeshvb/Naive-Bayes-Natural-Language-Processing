import sys
import os
file_permodel=open(os.path.dirname(os.path.abspath(sys.argv[0])) + "/per_model.txt", "r", encoding="latin1")
permodel_read=[]
for word in file_permodel:
    permodel_read.append(word)
WordList=[]


outfile=open(os.path.dirname(os.path.abspath(sys.argv[0])) + "//"+ sys.argv[2], "w", 1, "latin1")  

distictDic=dict()
for i in range(0,len(permodel_read)):
    newline=permodel_read[i].split(" ")
    if(i==0):
        biasVal=float(newline[1])
        print(biasVal)
    else:
        distictDic[newline[0]]=float(newline[1])
#print(distictDic)
file=[]
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    for fn in filenames:
        if ".txt" in fn:
            file.append(os.path.join(dirpath,fn))
            
for ha in file:
    file1=open(ha, "r", encoding="latin1")
    wordOfFiles=file1.read().split()
    file1.close()
    
    alphaVal=biasVal
    for wordInDictionary in wordOfFiles:
        if wordInDictionary in distictDic:
#             wordWeight=distictDic.get(wordInDictionary)
            alphaVal+=distictDic[wordInDictionary]
        
    if(alphaVal>0):
        outfile.write("spam "+str(ha))
        outfile.write('\n')
    else:
        outfile.write("ham "+str(ha))
        outfile.write('\n')
outfile.close()
        
            