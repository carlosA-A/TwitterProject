import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey=""
csecret=""
atoken=""
asecret=""


class listener(StreamListener):
    def on_status(self, status):
       
        try:
            textTweet= status.text+"\n"
            print(textTweet)
            saveFile = open("FileName.csv","a")
            saveFile.write(textTweet)
            saveFile.write("\n")
            saveFile.close()
            return True

        except BaseException as e:
            print("failed ondata",str(e))
            time.sleep(5)
    def on_error(self,status):
        print(status)




auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())

twitterStream.filter(track=["War"],languages = ['en'])
