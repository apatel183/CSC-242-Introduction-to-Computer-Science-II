##Lab9#####
##### Arpan Patel #####
# Question: 1 #

from html.parser import HTMLParser
from urllib.request import urlopen

# Question 1
class HeadingParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inheader = False
        self.headings = []
        self.lsttag= ['h1','h2','h3','h4','h5','h6']

    def handle_starttag(self, tag, attrs):
        if tag in self.lsttag:
            self.inheader = True 

    def handle_endtag(self, tag):
        if tag in self.lsttag:
            self.inheader = False

    def handle_data(self, data):
        if self.inheader == True:
            data=data.strip()
            if data != '':
                self.headings.append(data.strip())

    def getheadings(self):
        return self.headings

def testHP(url):
    HPtest = urlopen(url).read().decode()
    hpweb = HeadingParser()
    hpweb.feed(HPtest)
    return hpweb.getheadings()

#TEST
'''
>>> testHP('http://www.warnerbros.com/archive/spacejam/movie/cmp/sitemap.html')
[]
>>> testHP('http://www.pmichaud.com/toast/')
['Strawberry Pop-Tart Blow-Torches', 'Author', 'Abstract', 'Introduction', 'Materials Used', 'Experiment Preparation', 'The Experiment and Observations', 'Summary and Recommendations', 'Acknowledgements', 'Followup Comments']
>>> testHP('http://www.kli.org/')
['Home Page', 'The Klingon Language Institute', "Registration for qep'a' cha'maH cha'DIch (July 23rd - 25th, 2015) is now open!", 'Join the KLI today!', 'Klingon in a nutshell', 'Learn Klingon!']
>>> testHP('http://home.mcom.com/home/welcome.html')
['For More Information about Netscape...', 'Welcome to the world of Netscape', 'and the Internet.', 'Enjoy!']
>>> testHP('http://usatoday30.usatoday.com/sports/baseball/sbfant.htm')
['Fantasy baseball home page', 'Daily Best/Worst', "Baseball Weekly's John Hunt", 'Player position eligibility', 'Player ratings and projections', 'Other links of interest']
>>>
'''



if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab9TEST.py') )

