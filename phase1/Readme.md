<h2><b>libraries Used</b></h2>
PyStemmer
NLTK (SnowballStemmer)

<h2><b>How to run code</b></h2>
$bash roll_number/index.sh /home/wiki/multistream1.xml-p1p30303 roll_number/inverted_index/ roll_number/invertedindex_stat.txt
roll_number is the folder where we expect index.sh to be
  
This would generate two things in the same directory :
1.inverted_index - folder containing your inverted index - a single index file
2.invertedindex_stat.txt - file containing the stats 

<h2><b>Support for field queries</b></h2>

Index is supporting field search which we will be useful for phase 2  as well. But there are no field search queries for phase 1. Given a query, search will return the matched posting list(s) from index - which is human readable.


<b><h2>To search Run it like this:</b></h2>
$bash roll_number/search.sh roll_number/inverted_index/ query_string
Again, roll_number is the folder where we expect your search.sh to be
 
<b><h2>Plain query_string examples</b></h2>
Sachin Ramesh Tendulkar
Hogwarts

<b><h2>Field query_string examples</b></h2>
t:World Cup i:2019 c:Cricket
search for "World Cup" in Title, "2019" in Infobox and "Sports" in Category

t:the two towers i:1954
search for "the two towers" in Title and "1954" in Infobox

<b><h2>Phase 1 data links</b></h2>
https://drive.google.com/drive/folders/1G6_EmGdzxeIIIdHP9CEPKpxCsg4WUFRy?usp=sharing
https://wikimedia.bytemark.co.uk/enwiki/20200801/enwiki-20200801-pages-articles-multistream1.xml-p1p30303.bz2
http://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20200801/enwiki-20200801-pages-articles-multistream-index1.txt-p1p30303.bz2
https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20200801/enwiki-20200801-pages-articles-multistream1.xml-p1p30303.bz2
https://dumps.wikimedia.org/enwiki/20200801/enwiki-20200801-pages-articles-multistream1.xml-p1p30303.bz2

