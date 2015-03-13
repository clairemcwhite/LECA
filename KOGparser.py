from BeautifulSoup import BeautifulSoup as BS
import re
import csv

import urllib2

s = "KOGlist.txt"
s_input = open(s, "r")
KOGS = s_input.read().strip().split()
KOGS=list(KOGS) #this is a list of all the KOGS IDS


holder = []

#KOG = "KOG4383"
for KOG in KOGS:
    
    url = 'http://eggnog.embl.de/version_4.0.beta/cgi/search.py?search_term_0={0}&search_species_0=-1'.format(KOG)
    print url
    dictall = {}
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

  
    for line in sep3:
        

        
        words = line.split(':')
        
        species = words[0]
        genes = words[1]
        holder.append([KOG, species, genes])




f = open("KOGdictionary.csv", "w")
w = csv.writer(f)
for line in holder:
    w.writerow(line)

f.close()
