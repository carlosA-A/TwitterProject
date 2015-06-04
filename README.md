# TwitterProject
This is a simple program that searches twitter for tweets containing specific words. It creates a CSV file from where the stop words are removed and the words that appear repeated on the tweets are listed on a new text file called results.

Requirements:
tweepy
nltk

1-Insert the secret key and tokens on the file "Find tweet word hashtag.py"

2-At the bottom of that file writhe the word or hashtag you wish to search for track=["corvet"] and the language you are searching in languages = ['en'].

3-In saveFile = open("FileName.csv","a") name the file that will store all your tweets.

4-Run the application and stop it manually when enough tweets have been collected.

5-Open the application Stop checker and open the csv file we just created with all the tweets. file=open('FileName.csv', 'r')

6- The application will remove stop words and create a file called results.txt with the repeated words and the ammount of times they repeat.

 
