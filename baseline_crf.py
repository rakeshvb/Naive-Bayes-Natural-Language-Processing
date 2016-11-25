import hw3_corpus_tool
import sys
from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn
import pycrfsuite
from collections import Counter
import csv
import glob
import os
import time

print (time.strftime("%H:%M:%S"))
x=(sys.argv[1])

data = hw3_corpus_tool.get_data(x)
out=''
x_seq = []
y_seq = []

for act in data:
    
    flag=True
    speaker=''
    for i in act:
        third=[]
        #print(i)
        if flag:
            third.append('FU')
            
            flag=False
        if (speaker!=i[1]):    
            third.append('SC')
            speaker=i[1]
        if i[2]!=None:
            for z1 in i[2]:
                token='TOKEN_'+z1[0]
                third.append(token)
            for z in i[2]:
                pos='POS_'+z[1]
                third.append(pos)
        y_seq.append(i[0])    
        x_seq.append(third)
#first.append(second)

#print(len(x_seq))
#print(len(y_seq))

trainer = pycrfsuite.Trainer(verbose=False)


trainer.append(x_seq, y_seq)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-4,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True,
    'feature.possible_states': True
})

trainer.train('model.crfsuite')

tagger = pycrfsuite.Tagger()
tagger.open('model.crfsuite')




x1=(sys.argv[2])
count=0
file_count=0

file_name=(sys.argv[3])

dialog_filenames = sorted(glob.glob(os.path.join(sys.argv[2], "*.csv")))

for file_name in dialog_filenames:
    f = os.path.basename(file_name)
    #outfile.write("Filename=\""+f+"\"\n")
    out=out+"Filename=\""+f+"\"\n"
    data = hw3_corpus_tool.get_utterances_from_filename(file_name)
    flag=True
    speaker=''
    x_seq1=[]
    y_seq1=[]
    for i in data:
        third1=[]
       
        
        #print(i)
        if flag:
            third1.append('FU')
            
            flag=False
        if (speaker!=i[1]):    
            third1.append('SC')
            speaker=i[1]
        if i[2]!=None:
            for z1 in i[2]:
                token='TOKEN_'+z1[0]
                third1.append(token)
            for z in i[2]:
                pos='POS_'+z[1]
                third1.append(pos)
        #given = [third1]
        

        
        x_seq1.append(third1)
        
        y_seq1.append(i[0])
        file_count=file_count+1
    #print(x_seq1)
    y=tagger.tag(x_seq1)
    #print(y,'-',y_seq1)
    for l in y:
        index = y.index(l)
        #outfile.write(l+"\n")
        out=out+l+"\n"
        if l == y_seq1[index]:
            count+=1
            
            
    #outfile.write("\n") 
    out=out+"\n"       
        #y_seq1.append(i[0]) 
        #x_seq1.append(third1)
        
#This code calculates accuracy of evaluating directory, "x" has the value of accuracy
x=((count*100)/file_count)     
print(x)

outfile = open(sys.argv[3], "w", encoding='latin1')
outfile.write(out)
outfile.close() 
print (time.strftime("%H:%M:%S"))