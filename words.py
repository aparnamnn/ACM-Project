import facebook
token= "EAACEdEose0cBAFYJHuAlFZAPHKKdaFsYIA8aksdcRcI3XY6s97nZCF1Bi4Eqc6ToiCjkAzff7Bch4OWe3vwt7jJqTHff5A1FYWJIWJIH9t3O66jKDzrsK0LHWEW2NVTSbUIR9tY30GWe0f1tRSkNEgl3hiF7fqIIclk00YSG6iHZAEZArx3Er0wFSgjbX1MZD"
graph=facebook.GraphAPI(token)
profile=graph.get_object("379285459076775");
posts=graph.get_connections(profile['id'],"posts")
messages=[]
for post in posts['data']:
	try:
		messages.append(post['message'])
	except:
		continue
allwords=[]
for m in messages:
	words=m.split()
	for w in words:
		allwords.append(w);
		print w
wordfreq=[]
for w in allwords:
	wordfreq.append(allwords.count(w))
print("List"+str(allwords))
print("frequencies:"+str(wordfreq))
print("pairs"+str(zip(allwords,wordfreq)))
	
	

