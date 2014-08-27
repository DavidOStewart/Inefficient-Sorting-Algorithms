import sys
import random
import string

EOS = ['.','!','?']

def Generate_Dict(words):
    d = {}
    length = len(words)
    for index,element in enumerate(words):
        if index+2 < length:
            first = words[index]
            second = words[index+1]
            third = words[index+2]
            key = (first,second)
            if key not in d:
                d[key] = []
            d[key].append(third)
    return d

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def Generate_Sentence(d):
    begin = [key for key in d.keys() if key[0][0].isupper()]
        # gives list of all words starting with an uppercase
        # used to begin a sentence.
    key = random.choice(begin)
        # picks a random word to start the sentence

    li = [] #empty list, will be our sentence.
    first,second = key
    li.append(first)
    li.append(second)
    openquote = False
    while True:
        try:
            third = random.choice(d[key])
        except KeyError:
            break
        if not is_number(str.replace(third,' ', '')) and all(c in string.ascii_letters+str(EOS) for c in third):
            li.append(third)
        if third[0] == '"':
            openquote = True
        if not openquote:
            if third[-1] in EOS:
                break
        else:
            if third[-2] == '"':
                openquote = False
            if third[-1] == '"':
                openqote = False
        # else
        key = (second, third)
        first, second = key

    return ' '.join(li)

f = open('bible.txt','r')
words = f.read()
words = words.split()
dictionary = Generate_Dict(words)
sentence = ''
for x in range(20):
    sentence += '(' + str(x+1) + ') ' + Generate_Sentence(dictionary)  + ' '
print(sentence)
            
