 
import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got

def get_tweets():
   tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus').setSince("2020-01-01").setUntil("2020-06-30").setMaxTweets(1000)
   tweets = got.manager.TweetManager.getTweets(tweetCriteria)
   text_tweets=[[tweet.text] for tweet in tweets ]
   return text_tweets
  
    

    

text=""
text_tweets=get_tweets()
length= len(text_tweets)
#list to string
for i in range(0,length):
    text=text_tweets[i][0]+" "+text
#text=open('read.txt',encoding='utf-8').read()
lower_case=text.lower() #converting all words in lower case
#making text free of all punctuations.
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
#storing all words in a string- tokenization
tokenized_words=cleaned_text.split()
#stop words which does not add any meaning to our paragraphs
stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#finding words from cleaned_text and removing stop words from it
final_words=[]
for words in tokenized_words:
    if words  not in stop_words:
        final_words.append(words)


#now coming to our emotions.txt
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip() #clearing all the mess in emotion.txt
        words,emotion=clear_line.split(':')
    
        if words in final_words:
            emotion_list.append(emotion)     


w=Counter(emotion_list)
print(w)

fig , ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()