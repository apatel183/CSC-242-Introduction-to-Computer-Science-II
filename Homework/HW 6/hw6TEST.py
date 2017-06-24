# hw6TEST.py

>>> from hw6 import *


##### ImageCollector #####

>>> ic = ImageCollector('http://www2.warnerbros.com/spacejam/movie/jam.htm')
>>> ic.feed( urlopen('http://www2.warnerbros.com/spacejam/movie/jam.htm').read().decode())
>>> ic.getImages()=={'http://www2.warnerbros.com/spacejam/movie/img/p-sitemap.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-lunartunes.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jamlogo.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-junior.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-bball.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-studiostore.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-behind.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-souvenirs.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jump.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-pressbox.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-lineup.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jamcentral.gif'}
True

>>> ic = ImageCollector('http://www.kli.org/')
>>> ic.feed( urlopen('http://www.kli.org/').read().decode())
>>> ic.getImages()=={'http://www.kli.org/wp-content/uploads/2014/03/KLIbutton.gif', 'http://www.kli.org/wp-content/uploads/2014/03/KLIlogo.gif'}
True
>>> 

##### ImageCrawler #####

>>> c = ImageCrawler()
>>> c.crawl('http://www2.warnerbros.com/spacejam/movie/jam.htm',1,True)
>>> c.getImages()=={'http://www2.warnerbros.com/spacejam/movie/img/p-lunartunes.gif', 'http://www2.warnerbros.com/spacejam/movie/img/fast2.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-souvenirs.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-bball.gif', 'http://www2.warnerbros.com/spacejam/movie/cmp/pressbox/img/r-red.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-studiostore.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-bball.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-jamcentral.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jamlogo.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-lineup.gif', 'http://www2.warnerbros.com/spacejam/movie/img/fastbreak.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-sitemap.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-studiostore.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jump.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-junior.gif', 'http://www2.warnerbros.com/spacejam/movie/img/credits.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-junior.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-pressbox.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-behind.gif', 'http://www2.warnerbros.com/spacejam/movie/img/b-sitemap.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-sitemap.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-behind.gif', 'http://www2.warnerbros.com/spacejam/movie/img/littlelogo.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-jump.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-lunar.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-pressbox.gif', 'http://www2.warnerbros.com/spacejam/movie/img/break.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-lineup.gif', 'http://www2.warnerbros.com/spacejam/movie/img/pn-souvenirs.gif', 'http://www2.warnerbros.com/spacejam/movie/img/p-jamcentral.gif', 'http://www2.warnerbros.com/spacejam/movie/cmp/pressbox/img/r-blue.gif'}
True
>>> c = ImageCrawler()
>>> c.crawl('http://www.pmichaud.com/toast/',1,True)
>>> c.getImages()=={'http://www.pmichaud.com/toast/toast-6a.gif', 'http://www.pmichaud.com/toast/toast-2c.gif', 'http://www.pmichaud.com/toast/toast-4c.gif', 'http://www.pmichaud.com/toast/toast-6c.gif', 'http://www.pmichaud.com/toast/ptart-1c.gif', 'http://www.pmichaud.com/toast/toast-7b.gif', 'http://www.pmichaud.com/toast/krnbo24.gif', 'http://www.pmichaud.com/toast/toast-1b.gif', 'http://www.pmichaud.com/toast/toast-3c.gif', 'http://www.pmichaud.com/toast/toast-5c.gif', 'http://www.pmichaud.com/toast/toast-8a.gif'}
True


##### scrapeImages #####

>>> scrapeImages('http://www2.warnerbros.com/spacejam/movie/jam.htm','jam.html',1,True)
>>> open('jam.html').read().count('img')
62
>>> scrapeImages('http://www.pmichaud.com/toast/','toast.html',1,True)
>>> open('toast.html').read().count('img')
11
>>> 
