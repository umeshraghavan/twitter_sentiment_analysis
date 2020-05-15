
"""
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file 
named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet,

 and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, 
 in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, 
you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
"""

projectTwitterDataFile = open("/Users/umeshraghavan/Documents/Python_Learning/Twitter_Sentiment/project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '-']
# list of positive words to use
positive_words = []
with open("/Users/umeshraghavan/Documents/Python_Learning/Twitter_Sentiment/positive-words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("/Users/umeshraghavan/Documents/Python_Learning/Twitter_Sentiment/negative-words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#Takes one parameter, a string which represents a word, and removes characters considered punctuation 
# from everywhere in the word
def strip_punctuation(strWrd):
    string = strWrd
    for c in string:
        if c in punctuation_chars:
            string = string.replace(c,'')
    print(string)            
    return string

def get_pos(strSentences):
    str_check = strip_punctuation(strSentences)
    listStripSentence = str_check.split()
    count = 0
    for wrd in listStripSentence:
        for postitiveWord in positive_words:
            if wrd == postitiveWord:
                count += 1
    return count

def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()
    
    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count

def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    listpTDF = projectTwitterDataFile.readlines()
    headerNotUsed = listpTDF.pop(0)

    for listTD in listpTDF:
        listTD =  listTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")


writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()

