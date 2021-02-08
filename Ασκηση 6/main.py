#Programm that prints the 5 biggest and smallest words from the 10 latest tweets
#from the account that the user inputs

print("""\n Γράψτε ένα κώδικα σε Python ο οποίος συνδέεται στο twitter (χρησιμοποιείστε το tweepy)
και επιλέξτε τα 10 τελευταία tweets του χρήστη που θα σας δηλώσει ο χρήστης.
Εμφανίστε τις 5 μεγαλύτερες λέξεις και τις 5 μικρότερες λέξεις του. \n""")

import tweepy
import re

# Variables that contains the keys to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

#Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

#Create API object
api = connect_to_twitter_OAuth()


#Username input

username = input("Enter the Twitter username (without '@'): ")

#Makes the tweets list according to the username given
tweets = []
tweets_list = api.user_timeline(username, count=10, tweet_mode="extended")
for tweet in tweets_list:
    tweets.append(tweet.full_text)


#Prints the tweets list
for x in range(10):
    print(tweets[x], "\n")



#Removes linksand @
for i in range(10):
    tweets[i] = re.sub(r'http\S+', '', tweets[i])
    tweets[i] = re.sub(r'@\S+', '', tweets[i])
    tweets[i] = ''.join(i for i in tweets[i] if not i.isdigit())

#Removes punctuation
for i in range(10):
    tweets[i] = tweets[i].translate(str.maketrans('', '', string.punctuation))

#Removes emojis from tweets
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

for x in range(10):
    tweets[x] = remove_emoji(tweets[x])

#Makes a list with all the words separated
words = []
for j in range(10):
    splitted_words = tweets[j].split()
    words = words + splitted_words

#Sorts the list accoring to word size
sortwords = sorted(words, key=len, reverse=True)

#prints the 5 biggest words
biggest = '\n'
for i in range(5):
    biggest = biggest + sortwords[i] + '\n'

print("The 5 biggest words from this user's last 10 tweets are: ", biggest)

#prints the 5 smallest words
smallest = '\n'
for i in range(5):
    smallest = smallest + sortwords[len(sortwords)-1-i] + '\n'

print("The 5 smallest words from this user's last 10 tweets are: ", smallest)
