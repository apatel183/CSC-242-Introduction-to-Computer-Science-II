##Arpan Patel###
##hw6.py##

#Question 1 copied the file web.py#

#Question 2#

from web import LinkCollector
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError
#web.py file for the LinkColllector#


#Question 3#

class ImageCollector( HTMLParser ):
    def __init__(self,url):
        HTMLParser.__init__(self)
        self.url = url # remember url
        self.absoluteLinks = set()
        self.relativeLinks = set()
        self.collectimages = set() #collects in set()

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
        #looking for tag 'img' and attr is 'src'. 
        elif tag == 'img':
            for attr,value in attrs:
                if attr == 'src':
                    url= urljoin(self.url,value)
                    self.collectimages.add(url)

    def getRelatives(self):
        return self.relativeLinks
    def getAbsolutes(self):
        return self.absoluteLinks
    def getLinks(self):
        return self.relativeLinks.union( self.absoluteLinks )
    def getImages(self): #retireved images by this fuction# 
        return self.collectimages
#TEST
'''
>>> ic = ImageCollector('http://www2.warnerbros.com/spacejam/movie/jam.htm')
>>> ic.feed( urlopen('http://www2.warnerbros.com/spacejam/movie/jam.htm').read().decode())
>>> ic.getImages()
{'http://www2.warnerbros.com/spacejam/movie/img/p-sitemap.gif', …,  'http://www2.warnerbros.com/spacejam/movie/img/p-jamcentral.gif'}

>>> ic = ImageCollector('http://www.kli.org/')
>>> ic.feed( urlopen('http://www.kli.org/').read().decode())
>>> ic.getImages()
{'http://www.kli.org/wp-content/uploads/2014/03/KLIbutton.gif', 'http://www.kli.org/wp-content/uploads/2014/03/KLIlogo.gif'}
'''
##Question 4#

class ImageCrawler():

    def __init__(self):
        self.crawled = set()
        self.found = set()
        self.dead = set()
        self.crawlcollectionimages = set() #collection in set()
        
    
    def crawl(self,url,depth=0,relativeOnly=False):
        ''' recursively crawl url and collect links '''

        # collect images from url
        lc = ImageCollector(url)
        lc.feed( urlopen(url).read().decode() )
        # record the fact that we have crawled url
        self.crawled.add( url )

        # update found links
        if relativeOnly:
            found = lc.getRelatives()
        else:
            found = lc.getLinks()
            self.found.update( found )

        pictures= lc.getImages()
        self.crawlcollectionimages.update(pictures)#update pictures
    
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
    def getImages(self):#retireved images by this fuction## 
        return self.crawlcollectionimages

#TEST
'''
>>> c = ImageCrawler()
>>> c.crawl('http://www2.warnerbros.com/spacejam/movie/jam.htm',1,True)
>>> c.getImages()
{'http://www2.warnerbros.com/spacejam/movie/img/p-lunartunes.gif', … 'http://www2.warnerbros.com/spacejam/movie/cmp/pressbox/img/r-blue.gif'}
>>> c = ImageCrawler()
>>> c.crawl('http://www.pmichaud.com/toast/',1,True)
>>> c.getImages()
{'http://www.pmichaud.com/toast/toast-6a.gif', 'http://www.pmichaud.com/toast/toast-2c.gif', 'http://www.pmichaud.com/toast/toast-4c.gif', 'http://www.pmichaud.com/toast/toast-6c.gif', 'http://www.pmichaud.com/toast/ptart-1c.gif', 'http://www.pmichaud.com/toast/toast-7b.gif', 'http://www.pmichaud.com/toast/krnbo24.gif', 'http://www.pmichaud.com/toast/toast-1b.gif', 'http://www.pmichaud.com/toast/toast-3c.gif', 'http://www.pmichaud.com/toast/toast-5c.gif', 'http://www.pmichaud.com/toast/toast-8a.gif'}
'''

##Question 5#
    
def scrapeImages( url, filename, depth=0,relativeOnly=False):

    # collects images from url
    lc = ImageCrawler()
    lc.crawl( url,depth,relativeOnly)

    # write links to an filename
    htmlfile = open(filename,'w')
    htmlfile.write('<html><body>')
    for link in lc.getImages():
        htmlfile.write( '<img src={}>\n'.format(link))
    htmlfile.close()

#TEST
'''
>>> scrapeImages('http://www2.warnerbros.com/spacejam/
movie/jam.htm','jam.html',1,True)
>>> open('jam.html').read().count('img')
62
>>> scrapeImages('http://www.pmichaud.com/toast/',
'toast.html',1,True)
>>> open('toast.html').read().count('img')
11
'''
if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw6TEST.py'))








