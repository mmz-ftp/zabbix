{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/usr/bin/python\
\
import subprocess\
import json\
\
barman_list = subprocess.Popen(['barman','list-server'],stdout=subprocess.PIPE)\
\
value = \{'data':[] \}\
\
for line in barman_list.stdout:\
    server = line.split(' ')[0]\
    value['data'].append(\{'\{#SERVER\}':server\})\
print json.dumps(value)\
}