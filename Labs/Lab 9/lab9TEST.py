# lab9TEST.py

>>> from lab9 import *

##### testHP #####

>>> testHP('http://www.warnerbros.com/archive/spacejam/movie/cmp/sitemap.html')
[]
>>> testHP('http://www.pmichaud.com/toast/')
['Strawberry Pop-Tart Blow-Torches', 'Author', 'Abstract', 'Introduction', 'Materials Used', 'Experiment Preparation', 'The Experiment and Observations', 'Summary and Recommendations', 'Acknowledgements', 'Followup Comments']
>>> testHP('http://www.kli.org/')
['Home Page', 'The Klingon Language Institute', 'qep', 'a', 'cha', 'maH cha', 'DIch was a success!', 'Join the KLI today!', 'Klingon in a nutshell', 'Learn Klingon!']
>>> testHP('http://home.mcom.com/home/welcome.html')
['For More Information about Netscape...', 'Welcome to the world of Netscape', 'and the Internet.', 'Enjoy!']
>>> testHP('http://usatoday30.usatoday.com/sports/baseball/sbfant.htm')
['Fantasy baseball home page', 'Daily Best/Worst', "Baseball Weekly's John Hunt", 'Player position eligibility', 'Player ratings and projections', 'Other links of interest']
>>> 
