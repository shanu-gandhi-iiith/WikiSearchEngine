############BElIEVE IN GOD AND WORK HARD------------------ Everything else will fall in place
############# created by shanu gandhi on 30 -08- 2020

import time
import sys
import nltk
from nltk.stem import SnowballStemmer 
from nltk.corpus import stopwords
custset={" ","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could","redirect","couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "wiktionary", "cite","reflist"}
custset=custset.union(set(stopwords.words('english')))
ps =nltk.stem.SnowballStemmer('english')

indpath = sys.argv[1]
querystr = sys.argv[2]

##################
# read index file
count =-1
mapreaded={}
start=time.time();
with open(indpath+"index.txt") as fp: 
    while True:
        count=count+1
        # print(count,end=":")
        # print(time.time()-start)
        # if count==2:
        #   break
        line = fp.readline() 
        if not line: 
            break
        spls=line.split("=")
        wrd=spls[0]
        liststr=spls[1]
        # print(wrd)
        # print(lists)
        lis=liststr.split(":")
        ct=1
        biglis=[]
        lisins=[]
        for i in lis:
          # print(i, end=" ")
          lisins.append(i)
          if ct%7==0 and ct!=0:
            biglis.append(lisins)
            lisins=[]
            # print()
            # s1=0
          ct=ct+1
        mapreaded[wrd]=biglis

# print("time:", time.time()-start)


def searchinind(query):
  if len(query)==2:
    return
  lst=query[2:].split()
  for i in lst:
    if not (i in custset):
      stmd=ps.stem(i)
      # print(stmd)
      if stmd in mapreaded:
        print(mapreaded[stmd])


def searchnormal(query):
  stmq=ps.stem(query)
  # print("normal:",stmq)
  if stmq in mapreaded:
    print(mapreaded[stmq])


#####################main execution
q=querystr
q=q.lower()
if q[1]!=":":
  lis=q.split(' ')
  for i in lis:
    searchnormal(i)
else:
  j=0
  cs=""
  lis=q.split(' ')
  for i in lis:
    if i.startswith("t:") or i.startswith("r:") or i.startswith("e:") or i.startswith("b:") or i.startswith("i:") or i.startswith("c:") :
      # print(i[2:])
      searchnormal(i[2:])
    else:
      # print(i)
      searchnormal(i)