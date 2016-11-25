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

def get_shape(token):
    r = ''
    for c in token:
        if c.isupper():
            r += 'U'
        elif c.islower():
            r += 'L'
        elif c.isdigit():
            r += 'D'
        elif c in ('.', ','):
            r += '.'
        elif c in (';', ':', '?', '!'):
            r += ';'
        elif c in ('+', '-', '*', '/', '=', '|', '_'):
            r += '-'
        elif c in ('(', '{', '[', '<'):
            r += '('
        elif c in (')', '}', ']', '>'):
            r += ')'
        else:
            r += c
    return r


print (time.strftime("%H:%M:%S"))
x=(sys.argv[1])

data = hw3_corpus_tool.get_data(x)
out=''
x_seq = []
y_seq = []
countvalue=1
for act in data:
    
    flag=True
    speaker=''
    for i in act:
        third=[]
        #print(i)
        if flag:
            third.append('FU')
            
            flag=False
        if (act.index(i)==len(act)-1):
            third.append('LU')
        
        if (speaker!=i[1]):    
            third.append('SC')
            speaker=i[1]
        token_list = []
        pos_list = []
        
        if i[2]!=None:
            ll=len(i[2])
            third.append('POSTAG_LENGTH_'+str(ll))
            for z1 in i[2]:
                token='TOKEN_'+z1[0]
                third.append(token)
                third.append('TOKEN_LENGTH_'+str(len(z1[0])))
                token_list.append(z1[0])
                if len(token_list)>1:
                    #print(token_list)
                    ss=token_list.pop(0)
                    #ss=''
                    third.append('PREV_TOKEN_'+ss+'|TOKEN_'+z1[0])
                    ss=ss+'/'+z1[0]
                    third.append('SHAPE_'+get_shape(token))
                    #print(ss)
                    #third.append('TOKEN_BIGRAM'+ss)
                pos='POS_'+z1[1]
                third.append(pos)
                pos_list.append(z1[1])
                third.append('POS_LENGTH_'+str(len(z1[1])))
                if len(pos_list)>1:
                    ss1=pos_list.pop(0)
                    third.append('PREV_POS_'+ss1+'|POS_'+z1[1])
                    ss1=ss1+'/'+z1[1]
                    #third.append('POS_BIGRAM'+ss1)
                
            
        elif i[2]==None:
            third.append('POS_EMPTY_')
            third.append('POS_LENGTH_'+str(0))
            #countvalue=countvalue+1
        y_seq.append(i[0])    
        x_seq.append(third)
#first.append(second)

print(len(x_seq))
print(len(y_seq))

trainer = pycrfsuite.Trainer(verbose=False)


trainer.append(x_seq, y_seq)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-4,  # coefficient for L2 penalty
    'max_iterations': 100,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True,
    #'feature.possible_states': True
})

trainer.train('model1.crfsuite')
#print (time.strftime("%H:%M:%S"))

tagger = pycrfsuite.Tagger()
tagger.open('model1.crfsuite')




x1=(sys.argv[2])
count=0
file_count=0

file_name=(sys.argv[3])

dialog_filenames = sorted(glob.glob(os.path.join(sys.argv[2], "*.csv")))
countvalue1=1
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
        if flag:
            third1.append('FU')
            
            flag=False
        if (data.index(i)==len(data)-1):
            third.append('LU')
        if (speaker!=i[1]):    
            third1.append('SC')
            speaker=i[1]
        token_list = []
        pos_list = []
        
        if i[2]!=None:
            ll=len(i[2])
            third1.append('POSTAG_LENGTH_'+str(ll))
            for z1 in i[2]:
                token='TOKEN_'+z1[0]
                third1.append(token)
                third1.append('TOKEN_LENGTH_'+str(len(z1[0])))
                token_list.append(z1[0])
                third.append('SHAPE_'+get_shape(token))
                if len(token_list)>1:
                    ss=token_list.pop(0)
                    third1.append('PREV_TOKEN_'+ss+'|TOKEN_'+z1[0])
                    ss=ss+'/'+z1[0]
                    #third1.append('TOKEN_BIGRAM'+ss)
                pos='POS_'+z1[1]
                third1.append(pos)
                pos_list.append(z1[1])
                third1.append('POS_LENGTH_'+str(len(z1[1])))
                if len(pos_list)>1:
                    ss1=pos_list.pop(0)
                    third1.append('PREV_POS_'+ss1+'|POS_'+z1[1])
                    ss1=ss1+'/'+z1[1]
                    #third1.append('POS_BIGRAM'+ss1)
            
        elif i[2]==None:
            third1.append('POS_EMPTY_')
            third1.append('POS_LENGTH_'+str(0))
            #countvalue=countvalue+1
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

#This code calculates accuracy of evaluating directory, "x" has the value of accuracy
x=((count*100)/file_count)     
print(x)

outfile = open(sys.argv[3], "w", encoding='latin1')
outfile.write(out)
outfile.close() 
print (time.strftime("%H:%M:%S"))
