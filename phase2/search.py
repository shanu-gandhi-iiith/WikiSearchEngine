######################################################
#############          search part
############BElIEVE IN GOD AND WORK HARD------------------ Everything else will fall in place
############# created by shanu gandhi on 30 -08- 2020
######   sec ind format
# chunk_0:000
# chunk_1:incab
# chunk_2:variationsefncatherin
# chunk_3:efnnamesurfac
# chunk_4:postextorgwork550
import pickle
import nltk
import re
# nltk.download('punkt',quiet=True)
# nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize 
import math
import time
import sys
import nltk
from nltk.stem import SnowballStemmer 
from nltk.corpus import stopwords
custset={" ","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could","redirect","couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "wiktionary", "cite","reflist"}
custset=custset.union(set(stopwords.words('english')))
ps =nltk.stem.SnowballStemmer('english')

totalstr=""
# querystr = "3, t:World Cup i:2019 c:Cricket"

########output in queries_op.txt

##################
# read index file
count =-1
# mapreaded={}
start=time.time();

reslis=[]
map_docidattr={}
pickle_in = open("indexsf/dict.pickle","rb")
map_docidattr= pickle.load(pickle_in)


# print(len(map_docidattr))
# 't1-i3-c1-e3-b65-d38425':
def parseandsort(k, curdfull):
  global totalstr
  curlis=curdfull.split("=")
  curdoc=curlis[1].strip()
  # print("IN p&S",curdoc)
  ll=curdoc.split(":")
  # print(str(ll))
  ps=[]
  for i in ll:
    ilis=i.split("-")  ### [t1 i3 c1 e3 b65 d38425]
    cs=0
    for j in ilis: ##j=b65
      if j!="" and j!=" " and len(j)> 1 and j[0]!='d':
        # print(j,":",j[1:])
        ##### Assign weight to title =5X , infobox=3X, Categ= 3X, ext link=1.5X, Refs=1.5X, Body=1X
        if j[0]=='t':
          cs+=((int(j[1:]))*5)
        elif j[0]=='i':
          cs+=((int(j[1:]))*3)
        elif j[0]=='c':
          cs+=((int(j[1:]))*3)
        elif j[0]=='e':
          cs+=((int(j[1:]))*1.5)
        elif j[0]=='r':
          cs+=((int(j[1:]))*1.5)
        else:
          cs+=(int(j[1:]))
    docid=ilis[-1][1:]
    if cs >0 :
      ps.append([cs, docid]) 
  # print(str(ps))
  ps.sort(key=lambda x: x[0],reverse =True)
  # print(str(ps))
  for i in range( min(int(k),len(ps)) ):
    # print("11111")
    print((ps[i][1]),end =", ")
    print( map_docidattr[(ps[i][1])].split(":")[0])
    totalstr+=str(ps[i][1])+", "+str(map_docidattr[(ps[i][1])].split(":")[0])+"\n";





def parseandsortm(topK,reslis):
  global totalstr
  lisg=[]
  setdocs= set()
  for i1 in reslis:
    curdfull=i1
    # print(str(i1))
    curlis=curdfull.split("=")
    curdoc=curlis[1].strip()
    # print("IN p&S",curdoc)
    ll=curdoc.split(":")
    # print(str(ll))
    plsize=len(ll)
    # print("pls",plsize)
    # ps=[]
    ps={}
    for i in ll:

      ilis=i.split("-")  ### [t1 i3 c1 e3 b65 d38425]
      cs=0
      for j in ilis: ##j=b65
        if j!="" and j!=" " and len(j)> 1 and j[0]!='d':
            cs+=(int(j[1:]))

      docid=ilis[-1][1:]
      if cs >0 :
        tw=map_docidattr[docid].split(":")[-2]  ####### m1[58576] =   Phosphor:2:1:6:2622:38:2:2671:\n
        tf=math.log(1+(int(cs)/int(tw)))
        idf=math.log(len(map_docidattr)/int(plsize))
        tfidf=round(tf*idf, 10)
        ps[docid]=tfidf
        setdocs.add(docid)
    lisg.append(ps)
  lisf=[]
  for i in setdocs:
    cur=0
    ct=0
    for j in lisg:
      if i in j:
        cur+=j[i]
        ct=ct+1
    lisf.append([i,ct,cur])
  lisf = sorted(lisf, key = lambda x: (x[1], x[2]))
  lisf.reverse()
  for i in range( min(int(topK),len(lisf)) ):
    print((lisf[i][0]), end =", ")
    # print("11112")
    print( map_docidattr[(lisf[i][0])].split(":")[0])
    totalstr+=str(lisf[i][0])+", "+str(map_docidattr[(lisf[i][0])].split(":")[0])+"\n";


def parseandsortfield(topK,reslis):
  global totalstr
  # print(topK)
  lisg=[]
  setdocs= set()
  
  for i1 in reslis:
    # print(i)
    curtag=i1[0:1]
    curdfull=i1[2:]
#    print(str(curdfull))
    curlis=curdfull.split("=")
    curdoc=curlis[1].strip()
    # print("IN p&S",curdoc)
    ll=curdoc.split(":")
    # # print(str(ll))
    plsize=len(ll)
    # # print("pls",plsize)
    # ps=[]
    ps={}
    for i in ll:
      ilis=i.split("-")  ### [t1 i3 c1 e3 b65 d38425]
      cs=0
      for j in ilis: ##j=b65 ####adding all value here add only tag value req
        if j!="" and j!=" " and len(j)> 1 and j[0]!='d'and j[0]==curtag:
            cs+=(int(j[1:]))

      docid=ilis[-1][1:]
      if cs >0 :
        tw=map_docidattr[docid].split(":")[-2]  ####### m1[58576] =   Phosphor:2:1:6:2622:38:2:2671:\n
        tf=math.log(1+(int(cs)/int(tw)))
        idf=math.log(len(map_docidattr)/int(plsize))
        tfidf=round(tf*idf, 10)
        ps[docid]=tfidf
        setdocs.add(docid)
    lisg.append(ps)
  # for i in lisg:
  #   print(i)
  lisf=[]
  for i in setdocs:
    cur=0
    ct=0
    for j in lisg:
      if i in j:
        cur+=j[i]
        ct=ct+1
    lisf.append([i,ct,cur])
  lisf = sorted(lisf, key = lambda x: (x[1], x[2]))
  lisf.reverse()
  for i in range( min(int(topK),len(lisf)) ):
    print( (lisf[i][0]) ,end =", ")
    # print("333333")
    print( map_docidattr[(lisf[i][0])].split(":")[0])
    totalstr+=str(lisf[i][0])+", "+str(map_docidattr[(lisf[i][0])].split(":")[0])+"\n"




def searchnormal(query):
  global reslis
  stmq=ps.stem(query)
  # print("normal:",stmq)
  # sind=open("indexs/chunksf/secndind","r")
  sind=open("indexsf/chunksdir/secndind","r")
  sline =sind.readlines()
  ftosearch=""
  for i in range(len(sline)-1):
    curfw=sline[i].split(":")[1].strip()
    nextfw=sline[i+1].split(":")[1].strip()
    if curfw <= stmq and nextfw > stmq:
      ftosearch=sline[i].split(":")[0].strip()
      # print("found")
      break
  if ftosearch=="":
    ftosearch=sline[-1].split(":")[0].strip()
  # print("chunk to searc", ftosearch)
  fc=open("indexsf/chunksdir/"+ftosearch,"r")
  while True:
    line=fc.readline()
    if not line or line[0]>stmq[0]:
      break
    if line.startswith(stmq+"="):
      # print(line)
      reslis.append(line)
      break
  # print("")

def searchcateg(query):
  global reslis
  tag=query[0:1]
  query=query[2:]
  lisq=query.split()
  lisq.insert(0,tag)
  # print(lisq)
  curt=""
  sind=open("indexsf/chunksdir/secndind","r")
  sline =sind.readlines()
  for j in lisq:
    if j=='i' or j=='t'or j=='c'or j=='r'or j=='b'or j=='e':
      curt=j
      continue;
    stmq=ps.stem(j)
    # print(curt, ":",stmq)
    ftosearch=""

    for i in range(len(sline)-1):
      curfw=sline[i].split(":")[1].strip()
      nextfw=sline[i+1].split(":")[1].strip()
      if curfw <= stmq and nextfw > stmq:
        ftosearch=sline[i].split(":")[0].strip()
        # print("found")
        break
    
    if ftosearch=="":
      # print("line",sline)
      ftosearch=sline[-1].split(":")[0].strip()
    # print("chunk to searc", ftosearch)
    fc=open("indexsf/chunksdir/"+ftosearch,"r")
    while True:
      line=fc.readline()
      if not line or line[0]>stmq[0]:
        break
      if line.startswith(stmq+"="):
        # print(line)
        reslis.append(curt+":"+line)
        break
    # print("")
  return 




#####################   main execution

# readdocidtitle()
# querystr = "10, Narendra"
# querystr = "10, Shanu"

fq=open("queries.txt","r")
listqr=fq.readlines()

for i11 in listqr:
  # querystr="3, t:World Cup i:2019 c:Cricket"
  querystr=i11
  # print("\n\nquerystr is",querystr)
  q=querystr
  q=q.lower()
  qlis=q.split(",")
  topK=qlis[0]
  # print(topK)
  q=qlis[1]
  if q[2]!=":":
    st=time.time()
    # print("Norm str")
    reslis=[]
    lis=q.split(' ')
    for i in lis:
      if i!="":
        searchnormal(i)
    # print(reslis)
    if len(reslis)==0:
      print("No Document Found")
      totalstr+="No Document Found\n"
      pass
    elif len(reslis)==1:
      parseandsort(topK,reslis[0])
    else:
      # print("MULTIPLE WORDS")
      parseandsortm(topK,reslis)
    print(round(time.time()-st ,2),", ",round((time.time()-st)/int(topK) ,2))
    totalstr+=str(round(time.time()-st ,2))+", "+str(round((time.time()-st)/int(topK) ,2))+"\n"
  else:
    # print("Categ query")
    st=time.time()
    j=0
    cs=""
    q=q[1:]
    # print(q)
    lisq=q.split(":")
    # print(lisq)
    flis=[]
    cur=""
    flis.append(lisq[0]+":"+lisq[1][:-2])
    for i in range(len(lisq)-1):
      if i==0:
        continue
      if i==len(lisq)-2:
        cur=cur+lisq[i][-1]+":"+lisq[i+1]
      else:
        cur=cur+lisq[i][-1]+":"+lisq[i+1][:-1]
      cur=cur.strip()
      flis.append(cur)
      cur=""
    # print(flis)
    reslis=[]
    for i in flis:
      searchcateg(i)
    # print(len(reslis))
    # for i in reslis:
    #   print(i)
    if len(reslis)==0:
      print("No Document Found")
      totalstr+"No Document Found\n"
      pass
    else:
      # print("MULTIPLE DOCLIST")
      parseandsortfield(topK,reslis)
    print(round(time.time()-st ,2),", ",round((time.time()-st)/int(topK) ,2))
    totalstr+=str(round(time.time()-st ,2))+", "+str(round((time.time()-st)/int(topK) ,2));
  print("")
  totalstr+="\n\n"


fileo=open("queries_op.txt", "w+")
fileo.write(totalstr)
fileo.close()
