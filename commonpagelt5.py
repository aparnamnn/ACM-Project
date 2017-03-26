
def com_likes_lt_5(token) :
	graph=facebook.GraphAPI(token)
	profile=graph.get_object("me")
	friends = graph.get_connections("me", "friends")['data']
	friends_likes = { friend['name'] : graph.get_connections(friend['id'], "likes")['data'] 
		for friend in friends }
	my_likes = [ like['name'] 
             	for like in graph.get_connections("me", "likes")['data'] ]

	common_likes = list(set(my_likes) & set(friends_likes))
	count=len(common_likes);
	if count<5:
		return count
	else:
		return
