
#!/usr/bin/env python

# reference: http://hackaday.com/2015/06/05/astronaut-or-astronot-community-voting-begins/#comment-2595456

# get the actual data:
# - request voting page
# - extract project titles
# - return 'em as list
def getdata():
    import urllib2
    import re   
    response = urllib2.urlopen('http://hackaday.io/prize/vote')
    html = response.read().splitlines()
    hit = [re.sub('<[^<]+?>', '', s.rstrip().lstrip()) for s in html if "project-title" in s]
    return hit

# build histogram:
# - count item one up (if exists)
# - create item and set to one (if not exists/countup fails)
def pushhisto(histo,text):
    try:
        histo[text]+=1
    except:
        histo[text]=1

# we want a nice csv-ish output, so here is a simple formatting function
def printhisto(histo):
    print "-"*80
    for key, value in histo.iteritems() :
        print '"%s";%i'%(key,value)

# go for it:
histo = dict()

# 10k queries (=20k samples!) for nearly 600 possible answers
# so each possible answer should show up 20k/600 = 333 times in average
for i in range(0,10000):
    d = getdata()
    pushhisto(histo,d[0])
    pushhisto(histo,d[1])
    printhisto(histo)
    

    
