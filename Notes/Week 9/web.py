# web.py

# lab 9 posted, will be lab 10 next week
# one more hw, posted soon

##### html crash course #####
'''
sample.html - basic web page, text document

editor
    text editor
    wyswig editor - 

html - hypertext markup language

tags - generally, pair of tags, opening tag
       and a closing tag

     - opening tag, may have one or more
       attribute=value pair inside
       to set additional properties
'''

##### retrieving remote documents #####
'''
html documents are text documents

if html file is on the local computer, use open

for remote documents, use urllib.request


>>> from urllib.request import urlopen, urlretrieve
>>> 
>>> response = urlopen('http://cnn.com')
>>> html = response.read().decode()
>>> type( html )
<class 'str'>
>>> html[:100]
'<!DOCTYPE html><html class="no-js"><head><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatibl'
>>> 
>>> 
>>> html.count('web')
10
>>> html.count('<a')
207
>>> 
>>> # can also retrieve and save items
>>> 
>>> urlretrieve("http://www.surfertoday.com/images/stories/greatwhiteshark7.jpg","shark2.jpg")
('shark2.jpg', <http.client.HTTPMessage object at 0x02E83A30>)
>>> 
'''

##### html parsers #####
'''
parsing - read something in a structured fashion
        - chop something into useful bits

HTMLParser - parses (breaks up) an html
documnet into usable pieces.
when you 'feed" the parser it automatically
calls three methods as items are encountered

    handle_starttag
    handle_endtag
    handle_data - stuff in between tags

by default, these methods are stubs (placeholders,
implementation is pass)
But we can get the behaviour we want by
subclassing HTMLParser and
overriding these methods
'''

from html.parser import HTMLParser

class PrintParser( HTMLParser ):

    # feed, is inherited
    def handle_starttag(self,tag,attributes):
        print( 'handle_starttag', tag, attributes )

    def handle_endtag(self,tag):
        print( 'handle_endtag',tag)

    def handle_data(self,data):
        print( 'handle-data',data)

'''
>>> p = PrintParser()
>>> p.feed( open('sample.html').read() )
handle_starttag html []
handle-data 


handle_starttag head []
handle-data 

handle_starttag title []
handle-data  Sample HTML document 
handle_endtag title
handle-data 

handle_endtag head
handle-data
...
'''

##### LinkCollector #####

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class LinkCollector( HTMLParser ):
    ''' when constructed with a url, LinkCollector
collects all the links founded at the url.  you can
retrieve either relative links, absolute links, or
both (in relative form). '''

    def __init__(self,url):
        HTMLParser.__init__(self)
        self.url = url # remember url
        self.absoluteLinks = set()
        self.relativeLinks = set()

    def handle_starttag(self,tag,attrs):
        if tag=='a':
            # print(tag,attrs)
            # search for href in attributes
            for attr,value in attrs:
                if attr=='href':
                    # absolute
                    if value[:4]=='http':
                        self.absoluteLinks.add( value )
                    # relative
                    else:
                        # make absolute
                        url = urljoin(self.url,value)
                        # and remember
                        self.relativeLinks.add( url )

    def getRelatives(self):
        return self.relativeLinks
    def getAbsolutes(self):
        return self.absoluteLinks
    def getLinks(self):
        return self.relativeLinks.union( self.absoluteLinks )
                    
'''
>>> url = 'http://cnn.com'
>>> lc = LinkCollector( url )
>>> html = urlopen('http://cnn.com').read().decode()
>>> lc.feed( html )
>>> lc.getAbsolutes()
{'http://money.cnn.com/luxury/', 'http://cnn.it/go2', 'http://money.cnn.com/2016/02/29/investing/oil-prices-surge-opec/index.html', 'http://money.cnn.com/data/markets/', 'http://money.cnn.com/media/', 'http://money.cnn.com/technology/', 'http://bleacherreport.com/nfl', 'https://www.facebook.com/cnn', 'http://bleacherreport.com/world-football', 'http://www.turner.com', 'http://money.cnn.com/pf/', 'http://bleacherreport.com/college-football', 'http://bleacherreport.com/nba', 'http://twitter.com/cnn', 'http://instagram.com/cnn', 'http://cnn.it/20ZllpX', 'http://cnnnewsource.com', 'http://bleacherreport.com/mlb'}
>>>
'''

'''
make this work:
>>> scrapeLinks( url, filename ):
... creates an html document called filename
containing all the links found at url ...
'''

def scrapeLinks( url, filename ):

    # collects links from url
    lc = LinkCollector( url )
    lc.feed( urlopen(url).read().decode() )

    # write links to an filename
    htmlfile = open(filename,'w')
    htmlfile.write('<html><body>')
    for link in lc.getLinks():
        htmlfile.write( '<a href={}>{}</a><br>\n'.format(link,link))
    htmlfile.close()


##### Crawler #####

'''
make this work:
>>> c = Crawler()
>>> c.crawl('http://cnn.com',2,True)
... recursively crawl all links that are 2 clicks
from cnn, True means crawl relative links only ...
...
>>> c.getCrawled()
... returns a set of urls that were crawled (read) ...
>>> c.getFound()
... returns set of all links that have been found,
some may be bad links ...
>>> c.getDead()
... links found that were not loadable ...
'''

from urllib.error import URLError

class Crawler():

    def __init__(self):
        self.crawled = set()
        self.found = set()
        self.dead = set()
    
    def crawl(self,url,depth=0,relativeOnly=False):
        ''' recursively crawl url and collect links '''

        # collect links from url
        lc = LinkCollector(url)
        lc.feed( urlopen(url).read().decode() )
        # record the fact that we have crawled url
        self.crawled.add( url )

        # update found links
        if relativeOnly:
            found = lc.getRelatives()
        else:
            found = lc.getLinks()
        self.found.update( found )
    
        # base case, depth is zero
        if depth==0:
            return # quit, we are done        
        # otherwise recursively crawl links that were found
        # (reducing depth and paying attention to
        # relativeOnly)
        else:
            for link in found:
                if link not in self.crawled:
                    try:
                        self.crawl(link,depth-1,relativeOnly)
                    except (URLError, UnicodeDecodeError):
                        self.dead.add(link)
    
    def getCrawled(self):
        return self.crawled
    def getFound(self):
        return self.found
    def getDead(self):
        return self.dead
        
        
        
    

        

        
        


























