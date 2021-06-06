from numpy import save
import pandas as pd
from re import search
import sys
from lemmatisation_tools import lemmatise
import regex as re

csvname = sys.argv[1]
#print(csvname[len(csvname)-5])
def isEnglish(s):
    if len(s) < 35:
        return False
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def r_d(input):

    s = input
    l = s.split()
    k = []
    for i in l:
  
    # If condition is used to store unique string 
    # in another list 'k' 
        if (s.count(i)>=1 and (i not in k)or s.count(i)==1):
            k.append(i)
    return ' '.join(k)
from collections import Counter
  
def remov_duplicates(input):
  
    # split input string separated by space
    input = input.split(" ")
  
    # joins two adjacent elements in iterable way
    for i in range(0, len(input)):
        input[i] = "".join(input[i])
  
    # now create dictionary using counter method
    # which will have strings as key and their 
    # frequencies as value
    UniqW = Counter(input)
  
    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    return s
df = pd.read_csv(csvname)
saved_column = df.Message
for x in range(0, int(len(df))):
    if search(r"([a-fA-F\d]{40})", saved_column[x]) or not isEnglish(saved_column[x]):
        continue
    else:
        pass1 = remov_duplicates(saved_column[x])
        dupesremoved = re.sub(r'\b(\w+)( \1\b)+', r'\1', pass1)
        print(lemmatise(dupesremoved.rstrip()+". "), end = "")


