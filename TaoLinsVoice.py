import os
from markovbot35 import MarkovBot

#Reading Books
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath("__file__"))
book1 = os.path.join(dirname, 'Eeeeee_eee_eee.txt')
book2 = os.path.join(dirname, 'Shoplifting_From_American_Apparel.txt')
tweetbot.read(book1)
tweetbot.read(book2)
