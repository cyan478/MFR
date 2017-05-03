a = open("alice.txt", "r")
text = a.read().split()
a.close()

words = [word.strip('()",.!*\'-') for word in text]

def wordFreq(w):
  freq = filter(lambda a: a.lower() == w.lower(), words)
  return len(freq)
  
#test
print 'The frequency of the word "the" is ' + str(wordFreq('the'))
print 'The frequency of the word "is" is ' + str(wordFreq('is'))
print 'The frequency of the word "Alice" is ' + str(wordFreq('Alice'))

def totalFreq(w):
  freqs = [wordFreq(x) for x in w]
  return reduce(lambda a, b: a + b, freqs)
  
#test
print 'The total frequency of the words "the", "is", and "Alice" is ' + str(totalFreq(['the', 'is', 'Alice']))

def mostFreq():
  freqs = [[x, wordFreq(x)] for x in words]
  return reduce(lambda a, b: a if a[1] > b[1] else b, freqs)[0]

#test -- works, but takes a long time when using list comprehensions/map/filter/reduce
print 'The most frequently occurring word is ' + str(mostFreq())