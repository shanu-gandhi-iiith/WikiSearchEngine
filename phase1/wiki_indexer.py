############BElIEVE IN GOD AND WORK HARD------------------ Everything else will fall in place
############# created by shanu gandhi on 30 -08- 2020
#bash roll_number/index.sh 
              #/home/wiki/multistream1.xml-p1p30303  
              #roll_number/inverted_index/  
              #roll_number/invertedindex_stat.txt
#mnt/c/Users/Shanu/Desktop/2019201014

# python3 wiki_indexer.py /home/wiki/multistream1.xml-p1p30303 
                    #roll_number/inverted_index/ 
                    #roll_number/invertedindex_stat.txt
import sys 
import time
import os

totaltok=0
path = sys.argv[1]
indexpath = sys.argv[2] 
stats = sys.argv[3]

os.system("mkdir -p "+indexpath)
# print(xpath)
# print(indexpath)
# print(stats)

# import pickle 

##########################
import nltk
import re
nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize 

# import spacy
mapstem={}
custset={" ","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could","redirect","couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "wiktionary", "cite","reflist"}
# nlp = spacy.load('en')
custset=custset.union(set(stopwords.words('english')))
# custset=custset.union(set(spacy.lang.en.stop_words.STOP_WORDS))
ps =nltk.stem.SnowballStemmer('english')


informregex = re.compile(r'{{infobox(.*?)}}',re.DOTALL)
insidebrregex = re.compile(r'{\|(.*?)\|}',re.DOTALL)
linksremRegex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',re.DOTALL)
filermregex = re.compile(r'\[\[file:(.*?)\]\]',re.DOTALL)
citermregex = re.compile(r'{{v?cite(.*?)}}',re.DOTALL)
spsmrmregex = re.compile(r'[\'~` \n\"_!=@#$%-^*+{\[}\]\|\\<>/?]',re.DOTALL)

angbrregex = re.compile(r'<(.*?)>',re.DOTALL)
catRegExp = r'\[\[category:(.*?)\]\]'
nestedbrregex = re.compile(r'[-.,:;_?()"/\']',re.DOTALL)



def finalstr(body):
  global mapstem,totaltok
  body = body.lower()
  body = linksremRegex.sub(' ', body)
  body = insidebrregex.sub(' ', body) ##
  body = citermregex.sub(' ', body)
  body = angbrregex.sub(' ', body)  ##
  body = nestedbrregex.sub(' ', body)  ##
  body = filermregex.sub(' ', body)
  body = spsmrmregex.sub(' ', body)  ##
  body = informregex.sub(' ', body) ##

  body = body.replace('\'', '')
  body = body.strip()
  body = body.replace('\n', ' ')
  
  body = re.sub(' +', " ", body)
  body = re.sub("short description", " ", body)
  body=re.sub('[^a-zA-Z]', ' ', body)
  lis2=body.split()
  stmd=""
  for i in lis2:
    totaltok=totaltok+1
    if (not i in custset) and len(i) > 2:
      if i in mapstem:
        stmd+=mapstem[i]+" "
      else:
        x=ps.stem(i)
        mapstem[i]=x;
        stmd+=x+" "
  return (stmd)



# map making final
import re
import xml.sax

res=0
mapgl={}

titlestr="" 
infoboxstr=""
bodystr=""
categorystr="" 
extlinkstr=""
referencestr=""
cpid=-1
titleg=""
mapparid_id={}

def parsetxt_i_b_c(curline):
  curline=curline.lower()
  ib=""
  bd=""
  ct=""
  et=""
  rf=""
  lisw=curline.split()
  cflg=0
  iflg=0
  bal=0
  for wrd in lisw:
    if wrd.startswith("[[category"): # categs
      cflg=1
      iflg=0
      eflg=0
      rflg=0
    
    elif cflg==1 and wrd.startswith("]]"): ## cat end
      cflg=0;
      eflg=0
      rflg=0
    
    elif iflg==0 and wrd.startswith("{{infobox"): ## info start
      iflg=1
      bal=0
      cflg=0
      eflg=0
      rflg=0    

    if iflg==1:
      if wrd.find("{{"):
        bal=bal+1;
      if wrd.find("}}"):
        bal=bal-1;

    if bal==0 :
      iflg=0
      bal=0
        
    if cflg==1:
      ct+=wrd[11:]+" "

    elif iflg==1:
      ib+=wrd+" "
    
    elif cflg==0 and iflg==0:
      bd+=wrd+" "
  
  rs=bd.find("==references")
  if rs==-1 :
    rs=bd.find("== references")

  if  rs != -1 :
    re=bd.find("==",rs+18)
    if re==-1:
      rf+=bd[rs+16:]
      bd=bd[0:rs-1]
    else:
      rf+=bd[rs+16:re]
      bd=bd[0:rs-1] + bd[re+1: ]


  es=bd.find("== external links")
  if es==-1:
    es=bd.find("==external links")
  if es==-1:
    es=bd.find("=external links")
  if es==-1:
    es=bd.find("= external links")

  if es != -1 :
    ee1=bd.find("==", es+22)
    ee2=bd.find("[[ca", es+22)
    if ee1==-1 and ee2 ==-1:
      et+=bd[es+20:]
      bd=bd[0:es]
    elif ee1==-1 and ee2 !=-1:
      et+=bd[es+20:ee2]
      bd=bd[0:es]+bd[ee2:]
    elif ee1!=-1 and ee2==-1:
      et+=bd[es+20:ee1]
      bd=bd[0:es]+bd[ee1:]
    else:
      mn=min(ee1, ee2)
      et+=bd[es+20:mn]
      bd=bd[0:es]+bd[mn:]

  return ib, bd, ct,et,rf

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=""
        self.model=""
        self.speed=""
        self.title=""
        self.text=""
        self.parentid=-1
    
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        global res;
        if tag == "title":
            # print(res)
            res=res+1;
            # if (res %100) == 0 :
            #   print(res,": %s seconds " % (time.time() - start_time))
        
    def endElement(self, tag):
        global cpid,titleg;
        if (self.CurrentData =="title"):
            # print("PID T",cpid)
            # print("Title:",self.title)
            self.title=""
        
        elif (self.CurrentData =="parentid"):
            # print("Pid:",self.parentid)
            self.parentid=""
        elif (self.CurrentData =="text"):
            # print("Text",self.text)
            global infoboxstr, bodystr, categorystr, extlinkstr, referencestr,res
            
            # parse items from text
            infoboxstr, bodystr, categorystr, extlinkstr, referencestr=parsetxt_i_b_c(self.text)
            ###no print     
            titlestr=finalstr(titleg)
            infoboxstr=finalstr(infoboxstr)
            categorystr=finalstr(categorystr)
            extlinkstr=finalstr(extlinkstr)
            referencestr=finalstr(referencestr)
            bodystr=finalstr(bodystr)
            mapdoc={} #map< string ,lis[0,1,2,3,4,5]> lis[title,info,categ,ext,ref,body]
            
            #############enter in common doc map 0-title 1- info 2-categ 3-ext 4-ref 5-body
            
            listit=titlestr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[0]=v1[0]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[1,0,0,0,0,0]
            
            listit=infoboxstr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[1]=v1[1]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[0,1,0,0,0,0]
            
            listit=categorystr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[2]=v1[2]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[0,0,1,0,0,0]
            
            listit=extlinkstr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[3]=v1[3]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[0,0,0,1,0,0]
            
            listit=referencestr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[4]=v1[4]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[0,0,0,0,1,0]
            
            listit=bodystr.split(' ')
            for i in listit:
              if i in mapdoc:
                v1=mapdoc[i]
                v1[5]=v1[5]+1
                mapdoc[i]=v1
              else:
                mapdoc[i]=[0,0,0,0,0,1]
            
            # mapgl
            ##############            
            ###enter in global map
            for i in mapdoc:
              curlis=mapdoc[i]
              # curlis.append(cpid)
              mapparid_id[res]=titleg;
              curlis.append(res)
              if i in mapgl:
                cl=mapgl[i]
                cl.append(curlis)
                mapgl[i]=cl
              else:
                mapgl[i]=[curlis]
            

            
            #########
            infoboxstr=""
            bodystr=""
            categorystr=""
            extlinkstr=""
            referencestr=""
            
            self.text=""
        self.CurrentData=""
    
    def characters(self, content):
        global cpid,titleg
        if(self.CurrentData=="title"):
            self.title+=content
            titleg=content
        elif(self.CurrentData=="text"):
            self.text+=content
        elif(self.CurrentData=="parentid"):
            self.parentid=content
            cpid=content

start_time = time.time()

parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=XMLHandler()
parser.setContentHandler(Handler)
# parser.parse(pathsc)
parser.parse(path)
# print("done")
# print("--- %s seconds ---" % (time.time() - start_time))


# print(len(mapgl))

start_time=time.time()

# print("writing index file")
with open(indexpath+"index.txt", 'w') as writefile:
  for i in mapgl:
    if i =="":
      continue
    writefile.write(i+"=")
    for j in mapgl[i]:
      for k in j:
        writefile.write(str(k)+":")
    writefile.write("\n")
# print("--- %s seconds ---" % (time.time() - start_time))

with open(stats, 'w') as writefile:
  writefile.write(str(totaltok)+"\n")
  writefile.write(str(len(mapgl))+"\n")
