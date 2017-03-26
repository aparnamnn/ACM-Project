import facebook
from prettytable import PrettyTable

token='EAACEdEose0cBABGsK0JgStnQ9PWHr2JjEV3PTgPUaxn17Kwy9h9UtLvMz1Pmgf6FlAWeLpfUgZC8ZCPdoXdxpLmUMEIzVdD8pEMjkg2h0dLhYEUKf2txjHSuByarRpDrWGkdzr0qwCaEelKGSkmmeygRV9BdiBmwMcK7VA1K4soJ6HoSieZA3TZCD00wOnsZD'


graph=facebook.GraphAPI(token)

profile=graph.get_object("me")

friends = graph.get_connections("me", "friends")['data']

friends_likes = { friend['name'] : graph.get_connections(friend['id'], "likes")['data'] 
		for friend in friends }

my_likes = [ like['name'] 
             for like in graph.get_connections("me", "likes")['data'] ]

pt = PrettyTable(field_names=["Name"])
pt.align = 'l'
[ pt.add_row((ml,)) for ml in my_likes ]
print "My likes"
print pt

common_likes = list(set(my_likes) & set(friends_likes))

pt = PrettyTable(field_names=["Name"])

pt.align = 'l'

[ pt.add_row((cl,)) for cl in common_likes ]

print
print "My common likes with friends"
print pt


