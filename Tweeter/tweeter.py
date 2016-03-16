#import regex
import re
import csv
import pprint
import nltk.classify

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
    return pattern.sub(r"\1\1", s)
#end

#start process_tweet
def processTweet(tweet):
    # process the tweets
    
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)    
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end 

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
    featureVector = []  
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences 
        w = replaceTwoOrMore(w) 
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if it consists of only words
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
        #ignore if it is a stopWord
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector    
#end

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
	    features['contains(%s)' % word] = (word in tweet_words)
    return features
#end



#Read the tweets one by one and process it
inpTweets = csv.reader(open('data/training.csv', 'rb'))

stopWords = getStopWordList('data/stopwords.txt')

count = 0;
featureList = []
tweets = []
i=0;
for row in inpTweets:
    i=i+1
    #print "%s  "%(i)
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop

# Remove featureList duplicates
featureList = list(set(featureList))

"""
#for printing the feature words
for row in featureList:
  print row
"""

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, tweets)

print "\n\n   testing data uploaded\n wait .....\n"
# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
#print NBClassifier;

print "   classifier is fully trained  now ........"
""""
# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
print "testTweet = %s, sentiment = %s\n" % (testTweet, sentiment)
"""

""""
p=0
n=0
neu=0
while line:
    processedTestTweet=processTweet(line)
    sentiment=NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords)))
   # print " %s \n"%(sentiment)	
    if sentiment == "positive": p=p+1
    elif sentiment == "negative":n=n+1
    else: neu=neu+1
    line=fp.readline()
fp.close()

print "positive : %s  negative : %s   neutral : %s " %(p,n,neu)
"""



p=0;
n=0;
neu=0;
i=0;
#checkTweets = csv.reader(open('data/traning3.csv', 'rb'))
checkTweets = csv.reader(open('data/INC.csv', 'rb'))
for row in checkTweets:
       tweet = row[0]
       i=i+1
       #print "%d "%(i)
       processedTestTweet=processTweet(tweet)
       sentiment=NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords)))
       #print " %s \n"%(sentiment)	
       if sentiment == "positive": p=p+1
       elif sentiment == "negative":n=n+1
       else: neu=neu+1

print " Con \n positive : %s  negative : %s   neutral : %s \n\n\n " %(p,n,neu)
 
 
p=0;
n=0;
neu=0;
i=0;
#checkTweets = csv.reader(open('data/traning3.csv', 'rb'))
checkTweets = csv.reader(open('data/BJP.csv', 'rb'))
for row in checkTweets:
       tweet = row[0]
       i=i+1
       #print "%d "%(i)
       processedTestTweet=processTweet(tweet)
       sentiment=NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords)))
       #print " %s \n"%(sentiment)	
       if sentiment == "positive": p=p+1
       elif sentiment == "negative":n=n+1
       else: neu=neu+1

print " BJP \n positive : %s  negative : %s   neutral : %s \n\n\n" %(p,n,neu)
 

p=0;
n=0;
neu=0;
i=0;
#checkTweets = csv.reader(open('data/traning3.csv', 'rb'))
checkTweets = csv.reader(open('data/AAP.csv', 'rb'))
for row in checkTweets:
       tweet = row[0]
       i=i+1
       #print "%d "%(i)
       processedTestTweet=processTweet(tweet)
       sentiment=NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords)))
       #print " %s \n"%(sentiment)	
       if sentiment == "positive": p=p+1
       elif sentiment == "negative":n=n+1
       else: neu=neu+1

print " AAP \n positive : %s  negative : %s   neutral : %s \n\n\n" %(p,n,neu)
 
 
 
"""
# for ploting using matplot 
import matplotlib.pyplot as plt

D = {u'Postive':p, u'Negative': n, u'Neutral':neu }

plt.bar(range(len(D)), D.values(), align='center',color='black')
plt.xticks(range(len(D)), D.keys())

plt.show()
"""

