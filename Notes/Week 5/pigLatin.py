  
def pigLatin(string):
    '''translates a sentence (or word) consisting of lower case letters and spaces
from English to Pig Latin - not perfectly'''
    result = ''
    words = string.split()
    if len(words)>1:
        for word in words:
            result+=pigLatin(word)+' '
        result = result[:-1]
    else:
        string = string.strip()
        while len(string)!=0 and string[0].lower() not in 'aeiou':
            string = string[1:] + string[0]
        result = string + 'ay'
    return result
