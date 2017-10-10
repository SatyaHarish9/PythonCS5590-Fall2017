from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize
from nltk.stem import LancasterStemmer,WordNetLemmatizer
from nltk import pos_tag,ne_chunk,ngrams
from collections import Counter
import re
f=open("shakesphere.txt","r");
s=f.read();
print("contents of the text file\n",s);
stop_words=['a','an','the','and','are','as','for','has','in','is','it','was','by','.',',','?','!','(',')','we']
print("\n\n","When stopwords are removed\n")
sp=s.split()
reswords=[w for w in sp if w.lower() not in stop_words]
k=' '.join(reswords)
print(k,"\n")
fil_words=word_tokenize(k)
l=WordNetLemmatizer()
print("\n When Lemmatization is done:\n")
lemm=[];
for w in fil_words:
    lemm.append(l.lemmatize(str(w),pos="v"))
print(lemm)
tag=pos_tag(lemm)
rem_tag=[t for t in tag if t[1] not in ('VB','VBN')]
print("\nWhen verb words are removed\n ")
print("\n\n",rem_tag)
list2=[item[0] for item in rem_tag]
c=Counter(list2)
print("\n\n word frequency\n\n ",c,"\n")
rep=c.most_common(5)
print("\nTop five words that have been repeated most \n\n",rep)
most=[i[0] for i in rep]
print("\nAll the sentences with most repeated words \n\n")
sent=sent_tokenize(s);
z=""
for k in sent:
    if any(word in k for word in most):
        print(k)
        z=z+k
print("\nWhen all those sentences are concatenated\n")
print(z)
