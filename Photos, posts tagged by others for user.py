{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 import facebook\par
\par
token = "token"\par
\par
graph = facebook.GraphAPI(token)\par
\par
user = "me"\par
\par
profile = graph.get_object(user)\par
\par
friends = graph.get_connections(user, "friends")['data']\par
\par
user_name = profile['name']\par
\par
friends_names = [friend['name'] for friend in friends]\par
\par
print friends_names\par
\par
friends_posts = \{ friend['name'] : 0 for friend in friends \}\par
\par
posts_tagged_by_others = graph.get_connections(user, "posts", fields='from')['data']\par
\par
for posts_tagged_by_other in posts_tagged_by_others:\par
\tab name = posts_tagged_by_other['from']['name']\par
\tab if user_name != name:\par
\tab\tab if name in friends_names:\par
\tab\tab\tab friends_posts[name]+=1\par
\tab\tab else:\par
\tab\tab\tab friends_posts[name]=1\tab  \par
\par
friends_photos = \{ friend['name'] : 0 for friend in friends \}\par
\par
photos_tagged_by_others = graph.get_connections(user, "photos", fields='from')['data']\par
\par
for photos_tagged_by_other in photos_tagged_by_others:\par
\tab name = photos_tagged_by_other['from']['name']\par
\tab print name\par
\tab if user_name != name:\par
\tab\tab if name in friends_names:\par
\tab\tab\tab friends_photos[name]+=1\par
\tab\tab else:\par
\tab\tab\tab friends_photos[name]=1\par
\tab\tab\tab friends_names.append(name)\tab\tab\tab\par
print friends_posts\par
print friends_photos\par
}
 