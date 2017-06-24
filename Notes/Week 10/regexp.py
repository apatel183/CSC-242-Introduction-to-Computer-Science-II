# regexp.py

# final a week from today
# last hw due end of the week
# review on thursday

##### re - regular expressions #####

'''
regular expressions - match
strings based on patterns,
regular expressions are a language
for expressing the patterns

operators:

    . - matches any single character
    [] - give a list, match anything in the list
    [a-z] - gives a range, anythin a-z
    ^  - NOT,match anything but following character
         inside []
    |    - or
    () - grouping - will return matches groups as
         a tuple

special characters:
    \d - numeric digit [0-9]
    \D - not a numeric digit
    \s - whitespace character
    \S - not a whitespace
        \w - alphanumeric, equiv to [a-zA-Z0-9]?

number of matches:

    * - 0 or more matches of prev character (greedy)
    *? - same, but not greedy
    + - 1 or more matches of prev character
    ? - 0 or 1 of prev character
    {n} - exactly n of prev character
    {n,m} - matches anywhere from n to m of
            prev character, NOT pythonic, m is
            included

re.compile - when you compile a regular expression
you can do location searches for it in a string

>>> s = 'bt bet beet beeet bit bot bat hello hi bye (123) 456-7890   (666) 666-6666   abc@abc.com   frank@google.com '
>>> 
>>> s.find('bet')
3
>>> import re
>>> re.findall('bet',s)
['bet']
>>> re.findall('b.t',s)
['bet', 'bit', 'bot', 'bat']
>>> re.findall('b[ea]t',s)
['bet', 'bat']
>>> re.findall('b[(ea)(ou)]t','beat beet bout')
[]
>>> re.findall('b(ea)|(ou)t','beat beet bout')
[('ea', ''), ('', 'ou')]
>>> re.findall('(b)(ea)|(ou)(t)','beat beet bout')
[('b', 'ea', '', ''), ('', '', 'ou', 't')]
>>> re.findall('b(ea|ou)t','beat beet bout')
['ea', 'ou']
>>> re.findall('b[ea|ou]t','beat beet bout')
[]
>>> re.findall('(b(ea|ou)t)','beat beet bout')
[('beat', 'ea'), ('bout', 'ou')]
>>> re.findall('b.*',s)
['bt bet beet beeet bit bot bat hello hi bye (123) 456-7890   (666) 666-6666   abc@abc.com   frank@google.com ']
>>> re.findall('b.*t',s)
['bt bet beet beeet bit bot bat']
>>> re.findall('be*t',s)
['bt', 'bet', 'beet', 'beeet']
>>> re.findall('be+t',s)
['bet', 'beet', 'beeet']
>>> re.findall('be?t',s)
['bt', 'bet']
>>> re.findall('b^e',s)
[]
>>> s
'bt bet beet beeet bit bot bat hello hi bye (123) 456-7890   (666) 666-6666   abc@abc.com   frank@google.com '
>>> re.findall('b^et',s)
[]
>>> re.findall('b^[e]t',s)
[]
>>> re.findall('b[^e]t',s)
['bit', 'bot', 'bat']
>>> # find all strings of digits
>>> re.findall('\d+',s)
['123', '456', '7890', '666', '666', '6666']
>>> # email addresses
>>> re.findall('\.',s)
['.', '.']
>>> re.findall('\w+@\w+\.\w+',s)
['abc@abc.com', 'frank@google.com']
>>> # phone numbers
>>> re.findall('\(\d{3}\) \d\d\d-\d\d\d\d',s)
['(123) 456-7890', '(666) 666-6666']
>>> re.findall('(\(\d{3}\)) \d\d\d-\d\d\d\d',s)
['(123)', '(666)']
>>> # find all tags in hmtl document
>>> re.findall('<.+>',open('sample.html').read())
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    re.findall('<.+>',open('sample.html').read())
FileNotFoundError: [Errno 2] No such file or directory: 'sample.html'
>>> 
>>> 
>>> # something a little better for parsing
>>> # re.complie
>>> # re.compile
>>> s
'bt bet beet beeet bit bot bat hello hi bye (123) 456-7890   (666) 666-6666   abc@abc.com   frank@google.com '
>>> re.findall('b\wt',s)
['bet', 'bit', 'bot', 'bat']
>>> pattern = re.compile('b\wt') # same re
>>> pattern
re.compile('b\\wt')
>>> pattern.search(s)
<_sre.SRE_Match object; span=(3, 6), match='bet'>
>>> m = pattern.search(s)
>>> m.group()
'bet'
>>> m.start()
3
>>> m.end()
6
>>> m.span()
(3, 6)
>>> m = pattern.search(s,6)
>>> m
<_sre.SRE_Match object; span=(18, 21), match='bit'>
>>> m.group()
'bit'
>>> m.span()[1]
21
>>> 
    
'''
