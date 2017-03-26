import facebook

from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

import random



token='EAACEdEose0cBAHYBMbXyW9HwyJJIeCFBaWXEcLjsp3N0vB5HZApZCxqm7KQvVxb4fgF2ZA8nh625ZBJR3NzCMGc3ApU1MyZCYBwVF85LWxqdaEdt3cNVaS0y9CYsY4DDUjGcUeDZB0TMZBJwqdEBCZBClU00PeeMqnWmMpZCWCUFGmp12hZBZA3mLilYc450f4cWvkZD'



graph=facebook.GraphAPI(token)

profile=graph.get_object("me")



posts = graph.get_connections(profile['id'], 'posts')

messages=[]
for post in posts['data']:
	
	try:	
		
		messages.append(post['message'])
	
	except:
		continue


wordlist=[]

wordfr=[]

s=" "

for m in messages:
	
	words=m.split()
	
	for w in words:
		
		s=s+" "+w
		
		wordlist.append(w)
		
		print(w)

for w in wordlist:
	
	wordfr.append(wordlist.count(w))
print("List\n" + str(wordlist) + "\n")

print("Frequencies\n" + str(wordfr) + "\n")

print("Pairs\n" + str(zip(wordlist, wordfr)))

		
wordcloud = WordCloud(relative_scaling = 1.0,stopwords = 'to of').generate(s)

plt.imshow(wordcloud)

plt.axis("off")

plt.show()








