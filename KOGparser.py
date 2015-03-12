from BeautifulSoup import BeautifulSoup as BS
import re

import urllib2

s = "KOGlist.txt"
s_input = open(s, "r")
KOGS = s_input.read().strip().split()
KOGS=list(KOGS) #this is a list of all the KOGS IDS



dictall = {}
#KOG = "KOG4383"
for KOG in KOGS:
    url = 'http://eggnog.embl.de/version_4.0.beta/cgi/search.py?search_term_0={0}&search_species_0=-1'.format(KOG)
    print url

    page = urllib2.urlopen(url).read()
   

   
    newpage =  BS(page)
    description = newpage.findAll("div", {"class":"description"})
    description = re.sub('<[^<]+?>', '', str(description[0]))
    sep3 = []


    separate = description.split('\n')
    sep2 = [line for line in separate if line>0]
    for line in sep2:
        if line != '' and line[0]!=' ':
            sep3.append(line)

    #print sep3

    

    for line in sep3:
        
        words = line.split(' ')
        #print words
        species = words[1][:-1]
        #genes = words[0] + str(words[2:]
        dictall[species]= str(words[2:])

    #print dictall
    fulldict = {}
    fulldict[KOG]=dictall
print fulldict
    
