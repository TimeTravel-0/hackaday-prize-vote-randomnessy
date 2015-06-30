
# reference: http://hackaday.com/2015/06/05/astronaut-or-astronot-community-voting-begins/#comment-2595456


def getdata():
    import urllib2
    import re   
    response = urllib2.urlopen('http://hackaday.io/prize/vote')
    html = response.read().splitlines()
    hit = [re.sub('<[^<]+?>', '', s.rstrip().lstrip()) for s in html if "project-title" in s]
    return hit

def pushhisto(histo,text):
    try:
        histo[text]+=1
    except:
        histo[text]=1

def printhisto(histo):
    print "-"*80
    for key, value in histo.iteritems() :
        print '"%s";%i'%(key,value)

# go for it:
histo = dict()

for i in range(0,10000):
    d = getdata()
    pushhisto(histo,d[0])
    pushhisto(histo,d[1])
    printhisto(histo)
    

    
