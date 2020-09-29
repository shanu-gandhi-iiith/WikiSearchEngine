# WikiSearchEngine
A search engine to create index on wikipedia dump of around 50 GB and search efficiently with time constraint of 5 sec.
<h1>The General Information regarding phase 1 and phase 2 can be found in read me and documents inside their folder<h1>
 <h2>Other imlementation wise info for final phase is as follows</h2>
  For Index.py

Stemmer Used: SnowballStemmer
Optimisation to save time: Inserted stemmed words in map for each file during parsing a document
write name of files with path as multiline string it is splitted and  then index is made for each zip initially
also a file "globmap" is created and appended which will store docid(id starting with 0 for each document) and its corresponding title and count of words in title, index, category, externallinks, references, and body of that document seperated with ":" abd docid with "="

Index is stored as posting list in list of list format where each word entry correspond to list of list of 6 elements (t,i,c,e,r,b,d) 
to store in text file the fields are seperated with "-" while docid is ended with ":" to help in parsing
word=tval1-ival2-cval3-eval4-rval5-bval6-d:

After all files creation they are merged to a single file taking 2 file at a time .
After creating single file it is split in chunks and stored in chunksdir and a secondary index is made called "secind" containing staring word and filename of each chunk. A variable "chunksize" can be used to change chunk size which stores no of lines in each chunk.

The big index is deleted and also the globmap is stored in pickle format for fast retrieval.

For Search.py

First the query is parsed to identify a phrase or category query
If phrase query and single word it is fetchced normal search for posting list is done and returned in decresing order of weight calculated as (weight to title =5X , infobox=3X, Categ= 3X, ext link=1.5X, Refs=1.5X, Body=1X) times word count.
If multiple words query is there then tfidf value is calculated for each doc corresp a word and a set is used to store list of all words . Later for doc in set it is counted the occurence in the req words and also the value of tfidf is summed for each doc and then finally the list is made containing docid, count and tfidf of each document and sorted first on baisc of count and later on tfidf(as doc containg all words is more important)
same is done for field queries but only ther required fields are considerd.
