import xml.sax
import re
import string
import sys 
import time
import os
import nltk
import pickle
import re
nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize 
custset={" ","a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could","redirect","couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "wiktionary", "cite","reflist"}
# nlp = spacy.load('en')
custset=custset.union(set(stopwords.words('english')))
# custset=custset.union(set(spacy.lang.en.stop_words.STOP_WORDS))
ps =nltk.stem.SnowballStemmer('english')
reg1=re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',re.DOTALL)
reg2=re.compile(r'{{v?cite(.*?)}}',re.DOTALL)
reg3=re.compile(r'{\|(.*?)\|}',re.DOTALL)







# zippath = '''uz/enwiki-20200801-pages-articles-multistream1.xml-p1p30303
# uz/enwiki-20200801-pages-articles-multistream2.xml-p30304p88444
# uz/enwiki-20200801-pages-articles-multistream3.xml-p88445p200509
# uz/enwiki-20200801-pages-articles-multistream4.xml-p200510p352689
# uz/enwiki-20200801-pages-articles-multistream5.xml-p352690p565313
# uz/enwiki-20200801-pages-articles-multistream6.xml-p565314p892912
# uz/enwiki-20200801-pages-articles-multistream7.xml-p892913p1268691
# uz/enwiki-20200801-pages-articles-multistream8.xml-p1268692p1791079
# uz/enwiki-20200801-pages-articles-multistream9.xml-p1791080p2336422
# uz/enwiki-20200801-pages-articles-multistream10.xml-p2336423p3046512
# uz/enwiki-20200801-pages-articles-multistream11.xml-p3046513p3926861
# uz/enwiki-20200801-pages-articles-multistream12.xml-p3926862p5040436
# uz/enwiki-20200801-pages-articles-multistream13.xml-p5040437p6197594
# uz/enwiki-20200801-pages-articles-multistream14.xml-p6197595p7697594
# uz/enwiki-20200801-pages-articles-multistream14.xml-p7697595p774
# uz/enwiki-20200801-pages-articles-multistream15.xml-p7744801p9244800
# uz/enwiki-20200801-pages-articles-multistream15.xml-p9244801p9518048
# uz/enwiki-20200801-pages-articles-multistream16.xml-p9518049p11018048
# uz/enwiki-20200801-pages-articles-multistream16.xml-p11018049p11539266
# uz/enwiki-20200801-pages-articles-multistream17.xml-p11539267p13039266
# uz/enwiki-20200801-pages-articles-multistream17.xml-p13039267p13693073
# uz/enwiki-20200801-pages-articles-multistream18.xml-p13693074p15193073
# uz/enwiki-20200801-pages-articles-multistream18.xml-p15193074p16120542
# uz/enwiki-20200801-pages-articles-multistream19.xml-p16120543p17620542
# uz/enwiki-20200801-pages-articles-multistream19.xml-p17620543p18754735
# uz/enwiki-20200801-pages-articles-multistream20.xml-p18754736p20254735
# uz/enwiki-20200801-pages-articles-multistream20.xml-p20254736p21222156
# uz/enwiki-20200801-pages-articles-multistream21.xml-p21222157p22722156
# uz/enwiki-20200801-pages-articles-multistream21.xml-p22722157p23927983
# uz/enwiki-20200801-pages-articles-multistream22.xml-p23927984p25427983
# uz/enwiki-20200801-pages-articles-multistream22.xml-p25427984p26823660
# uz/enwiki-20200801-pages-articles-multistream23.xml-p26823661p28323660
# uz/enwiki-20200801-pages-articles-multistream23.xml-p28323661p29823660
# uz/enwiki-20200801-pages-articles-multistream23.xml-p29823661p30503450
# '''
zippath = '''uz/enwiki-20200801-pages-articles-multistream1.xml-p1p30303
uz/enwiki-20200801-pages-articles-multistream2.xml-p30304p88444
'''

indexpath = "indexsf"
stats = "stats.txt"

mapparid_id={} ###map of title vs id
res=0 ############### make unique id
mapstem={} ##### stm wrd map
totaltok=0

os.system("mkdir -p "+indexpath)

######################################global upto here
uziplis=zippath.split()
## run for each file
print("start for loop")
for indct in range(len(uziplis)):
	cfile=uziplis[indct]
	print("cfile")
	#custom functions

	def rem_pun(line):
	    return line.translate(str.maketrans('','',string.punctuation))


	def hasNumbers(instr):
	    return any(char.isdigit() for char in instr)

	def finalstr(body):
	  global mapstem,totaltok
	  body = body.lower()
	  body = reg1.sub(' ', body)
	  body = reg2.sub(' ', body)
	  body = reg3.sub(' ', body)
	  body=body.replace('"', ' ')
	  body=body.replace("'", ' ')
	  body = rem_pun(body)
	  lis2=body.split()

	  stmd=""
	  for i in lis2:
	    totaltok=totaltok+1
	    if (not i in custset) and len(i) > 2 and len(i)<=30:
	      i=i.replace('"', '')
	      i=i.replace("'", '')
	      if i in mapstem:
	        stmd+=mapstem[i]+" "
	      else:
	        x=ps.stem(i)
	        mapstem[i]=x;
	        stmd+=x+" "
	  return (stmd)


	mapgl={}

	titlestr="" 
	infoboxstr=""
	bodystr=""
	categorystr="" 
	extlinkstr=""
	referencestr=""
	cpid=-1
	titleg=""


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
	            print(res)
	            res=res+1;
	            if (res %100) == 0 :
	              print(res,": %s seconds " % (time.time() - start_time))
	        
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
	            counttit,counti,countc,countb,counte,countr=0,0,0,0,0,0,
	            # parse items from text
	            infoboxstr, bodystr, categorystr, extlinkstr, referencestr=parsetxt_i_b_c(self.text)
	            ###no print
	            # print(finalstr(bodystr))     
	            titlestr=finalstr(titleg)
	            infoboxstr=finalstr(infoboxstr)
	            categorystr=finalstr(categorystr)
	            extlinkstr=finalstr(extlinkstr)
	            referencestr=finalstr(referencestr)
	            bodystr=finalstr(bodystr)
	            mapdoc={} #map< string ,lis[0,1,2,3,4,5]> lis[title,info,categ,ext,ref,body]
	            
	            #############enter in common doc map 0-title 1- info 2-categ 3-ext 4-ref 5-body
	            
	            listit=titlestr.split(' ')
	            counttit+=len(listit)
	            for i in listit:
	              if i in mapdoc:
	                v1=mapdoc[i]
	                v1[0]=v1[0]+1
	                mapdoc[i]=v1
	              else:
	                mapdoc[i]=[1,0,0,0,0,0]
	            
	            listit=infoboxstr.split(' ')
	            counti+=len(listit)
	            for i in listit:
	              if i in mapdoc:
	                v1=mapdoc[i]
	                v1[1]=v1[1]+1
	                mapdoc[i]=v1
	              else:
	                mapdoc[i]=[0,1,0,0,0,0]
	            
	            listit=categorystr.split(' ')
	            countc+=len(listit)
	            for i in listit:
	              if i in mapdoc:
	                v1=mapdoc[i]
	                v1[2]=v1[2]+1
	                mapdoc[i]=v1
	              else:
	                mapdoc[i]=[0,0,1,0,0,0]
	            
	            listit=extlinkstr.split(' ')
	            counte+=len(listit)
	            for i in listit:
	              if i in mapdoc:
	                v1=mapdoc[i]
	                v1[3]=v1[3]+1
	                mapdoc[i]=v1
	              else:
	                mapdoc[i]=[0,0,0,1,0,0]
	            
	            listit=referencestr.split(' ')
	            countr+=len(listit)
	            for i in listit:
	              if i in mapdoc:
	                v1=mapdoc[i]
	                v1[4]=v1[4]+1
	                mapdoc[i]=v1
	              else:
	                mapdoc[i]=[0,0,0,0,1,0]
	            
	            listit=bodystr.split(' ')
	            countb+=len(listit)
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
	              mapparid_id[res]=[titleg,counttit,counti,countc,countb,counte,countr,(counttit+counti+countc+countb+counte+countr)]
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
	print("start parsing")
	parser=xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=XMLHandler()
	parser.setContentHandler(Handler)
	# parser.parse(pathsc)
	parser.parse(cfile)
	print("done")
	print("--- %s seconds ---" % (time.time() - start_time))


	print(len(mapgl))

	start_time=time.time()


	mapgl3={}

	for key in (mapgl):
	  i2=key
	  i2=i2.replace("'","")
	  i2=i2.replace('"',"")
	  i2=i2.replace('-',"")
	  # i2=re.sub(r'[^A-Za-z0-9 ]+', '', i2)
	  if i2 =="":
	    continue
	  mapgl3[i2]=mapgl[key]

	mapgl=mapgl3
	mapgl2={}
	for key in sorted(mapgl):
	    mapgl2[key]=mapgl[key]

	print("writing index file")

	with open(indexpath+"/ind"+str(indct), 'w') as writefile:
	  for i in mapgl2:
	    if i =="":
	      continue
	    writefile.write(i+"=")
	    for j in mapgl2[i]:
	      ind=-1
	      for k in j:
	        ind=ind+1
	        if k==0:
	          continue #map< string ,lis[0,1,2,3,4,5]> lis[title,info,categ,ext,ref,body,docid()]
	        if ind==0:
	          writefile.write("t"+str(k)+"-")
	        if ind==1:
	          writefile.write("i"+str(k)+"-")
	        if ind==2:
	          writefile.write("c"+str(k)+"-")
	        if ind==3:
	          writefile.write("e"+str(k)+"-")
	        if ind==4:
	          writefile.write("r"+str(k)+"-")
	        if ind==5:
	          writefile.write("b"+str(k)+"-")
	        if ind==6:
	          writefile.write("d"+str(k)+":")
	    writefile.write("\n")
	print("--- %s seconds ---" % (time.time() - start_time))


	with open("globmap", 'a+') as writefile:
	  for i in mapparid_id:
	    str2=""
	    for k in mapparid_id[i]:
	      str2+=str(k)+":"
	    # print(str(i)+"="+str2+"\n")
	    writefile.write(str(i)+"="+str2+"\n")

############################
# End of Part 1
############################

# 	print("--- %s seconds ---" % (time.time() - start_time))

import os
path="indexsf";

finidname=""
###############   function to merge 2 files 
def merge2f(file1, file2, file3):
  import os
  #actual merge 2 files
  # !head -10 "drive/My Drive/IRE/phase2/textindex2.txt"
  file1 = open(file1, 'r') 
  file2 = open(file2, 'r') 
  file3 = open(file3, 'w+') 
  count=0
  line1 = file1.readline() 
  line2 = file2.readline() 
  while line1 or line2:
    if line1 and not line2:
      file3.write(line1)
      line1=file1.readline()
    elif line2 and not line1:
      file3.write(line2)
      line2=file2.readline()
    else:
      line10=line1.split("=")[0]
      line20=line2.split("=")[0]
      if (line10 < line20):
        file3.write(line1)
        line1=file1.readline()
      elif (line10 > line20):
        file3.write(line2)
        line2=file2.readline()
      else:
        linecommon=""
        linecommon=linecommon+line10+"="
        res=""
        res =res+line1.split("=")[1][:-1]
        res =res+line2.split("=")[1]
        
        linecommon=linecommon+res
        file3.write(linecommon)
        line1=file1.readline()
        line2=file2.readline()
  file1.close() 
  file2.close() 
  file3.close() 


j=11
while True:
  fileslis=[]
  for filename in os.listdir(path):
    fileslis.append(path+"/"+filename)
  if len(fileslis)==1:
    break
  i=0
  while i < (len(fileslis))-1:
    merge2f(fileslis[i],fileslis[i+1],path+"/"+str(j))
    finidname=str(j)
    os.remove(fileslis[i])
    os.remove(fileslis[i+1])
    j=j+2
    i=i+2
# import os
os.system("mv indexsf/"+finidname+"  indexsf/indmerged")


# ##########################################
# # end of part 2 common merged index build
# ##########################################



#################split index and create small files
import os
os.system("mkdir -p indexsf/chunksdir")

indf=open("indexsf/chunksdir/secndind","w")

readf=open("indexsf/indmerged","r")
line = readf.readline() 
# j=-1
j=-1

chunksize=500000
writefile=open("indexsf/chunksdir/chunk_0","w")
indf.write("chunk_0:"+str(line.split("=")[0])+"\n")
while True:
	j=j+1
	# if j==30003:
	# 	break
	if not line: 
		break
	if j%chunksize==0 and j!=0:
		indf.write("chunk_"+str(int(j/chunksize))+":"+str(line.split("=")[0])+"\n")
		writefile.close()
		writefile=open("indexsf/chunksdir/chunk_"+str(int(j/chunksize)), "w")

	writefile.write(line)
	line = readf.readline() 
	if not line: 
		break
writefile.close()
readf.close()
indf.close()

########dump in pickle
map_docidattr={}
f1=open("globmap","r")
# line= 58576=Phosphor:2:1:6:2622:38:2:2671:
while True:
  line=f1.readline()
  if not line:
    break
  line=line.strip()
  did=line.split("=")[0]
  attr=line.split("=")[1]
  map_docidattr[did]=attr

pickle_out = open("indexsf/dict.pickle","wb")
pickle.dump(map_docidattr, pickle_out)
pickle_out.close()
os.system("rm indexsf/indmerged")
os.system("rm globmap")
