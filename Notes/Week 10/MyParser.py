# MyParser.py - our own HTMLParser from scratch
# doesnt subclass

import re

class MyParser():
    ''' mimics behavior of HTMLParser'''

    # init?

    def handle_tag(self,tag):
        ''' given either start end tag, calls appropriate
            handle method'''
        #print(tag)
        # if end tag, call handle_endtag
        if tag[0]=='/':
            self.handle_endtag(tag[1:])
        else: # opening tag
            # assume attributes
            # are written attr=value, without spaces
            typePattern = re.compile('\w+')
            m = typePattern.search(tag)
            pairPattern = re.compile('(\w+)=(\S+)')
            # can make a fancier version which hanldes spaces
            attrs = pairPattern.findall(tag)
            self.handle_starttag(m.group(),attrs)
                                

    def handle_starttag(self,tag,attrs):
        print('hst:',tag,attrs)

    def handle_endtag(self,tag):
        print('het:',tag)

    def handle_data(self,data):
        print('hd:',data)
        pass

    def feed(self,html):
        ''' parses the string html, calls appropriate
handle methods with arguments'''

        i=0 # index of cursor location

        # pattern for tag
        tagPattern = re.compile('<.*?>')


        # loop through string, increasing
        # cursor location
        while i<len(html)-1:

            # look for a tag
            m = tagPattern.search(html,i)
    
            # anythin before found location
            # is data
            data = html[i:m.start()] # may be empty
            self.handle_data(data)

            # read tag without < and >
            # and process
            tag = html[m.start()+1:m.end()-1]
            self.handle_tag( tag )

            # increase cursor
            i = m.end()
        


















        

    

