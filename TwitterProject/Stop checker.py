import itertools
import operator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer



def removeStop():
    emptyList=[]
    tokenizer = RegexpTokenizer("[\w']+")
    #Open Doc with stop words and twitter words to remove
    word_list = open("Stop.txt", "r")

    with word_list as text_file:
            text = text_file.read()
            tokenizer = RegexpTokenizer(r'\w+')
            stopWordList=tokenizer.tokenize(str(text))

    #Open csv file with tweets downloaded and tokenize them
    file=open('Corvet.csv', 'r')
    with file as text_file:
        text = text_file.read()
        tokenizer = RegexpTokenizer(r'\w+')
        tweetTokens=tokenizer.tokenize(str(text))
        #print(tokenizedFile)

    
    for i in tweetTokens:
        if i.lower() in stopWordList:
            pass
        else:
           emptyList.append(i)

##    
##    commonW=most_common(emptyList)
##    #print (emptyList)
##    #print(commonW)
##    popular=0
##    for i in emptyList:
##        if i == str(commonW):
##            popular+=1


    popularWords(emptyList)


    word_list.close()
    file.close()


def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def popularWords(listTa):
    b=list(listTa)
    c=[]
    textF=open("results.txt","w")
    for i in b:
        w=0
        for x in b:
            if i.lower()==x.lower():

                w+=1
        #If word repeated more than 40 times then return that word with the ammount of times it repeats        
        if w>40 and (i.lower()+" "+ str(w)) not in c:
            result= i.lower()+" " +str(w)
            
            c.append(result)
            textF.write(result+"\n")

    print (c)
    textF.close()
removeStop()
