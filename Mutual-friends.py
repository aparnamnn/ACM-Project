{\rtf1\ansi\ansicpg1252\cocoartf1347\cocoasubrtf570
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 import facebook\
import json\
\
token = \'93token\'94\
graph = facebook.GraphAPI(token)\
user = \'93me\'94\
profile = graph.get_object(user)\
friends = graph.get_connections(user,\'94friends\'94)[\'91data\'92]\
user_name = profile[\'91name\'92]\
friends_names = [friend[\'91name\'92] for friend in friends]\
print friends_names}