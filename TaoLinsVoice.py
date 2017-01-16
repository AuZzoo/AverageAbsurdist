import os
from markovbot35 import MarkovBot

#Reading Books
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath("__file__"))
book1 = os.path.join(dirname, 'Eeeeee_eee_eee.txt')
book2 = os.path.join(dirname, 'Shoplifting_From_American_Apparel.txt')
tweetbot.read(book1)
tweetbot.read(book2)

#Twitter auth
cons_key = 'CdCzXicQ1KrfDCArbQpryM7hM'
cons_secret = 'DbU1njCMps99B37boiTjcS9TPoymHrVx7rrpz7em5roDKC4BPU'
access_token = '820759897184686080-SherqvQ5cOv6vDnZJni0ORZiGclMUM8'
access_token_secret = 'TBoLU4dfUVhRwSQRXAIqPIAggsd6R3TzhhdXtyJtV681V'

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

#Reply to: 
targetstring = '@cooliotonyio' 
tweetbot.twitter_autoreply_start(targetstring, keywords = None, prefix = None, suffix = None, maxconvdepth = None)

tweetbot.twitter_tweeting_start(days = 0, hours = 10, minutes = 0, keywords = None, prefix = None, suffix = None) 
