from BeautifulSoup import BeautifulSoup as BS
import re
import csv

import urllib2

s = "KOGlist.txt"
s_input = open(s, "r")
KOGS = s_input.read().strip().split()
KOGS=list(KOGS) #this is a list of all the KOGS IDS

#KOGS = KOGS[0:1]
holder = []
count = 0
#KOG = "KOG4383"
for KOG in KOGS:
    
    url = 'http://eggnog.embl.de/version_4.0.beta/cgi/search.py?search_term_0={0}'.format(KOG)
    print count
    count = count + 1
    dictall = {}
    page = urllib2.urlopen(url).read()

   
 
    newpage =  BS(page)

    info = newpage.findAll("div", {"class":"name"})
    #print species
    #test = info[1].split("\n")
    info = str(info[1])
    
    info = info.split("\n")

    spec = str(info[2]).replace('<font class="small_light">', "")
    spec = spec.replace('</font>', "")
    #spec = re.sub('<[^>]+?>', '', str(info[2]))
    #print spec
    
    group = str(info[4]).replace('<font class=\"small_light\">FC: <font title="', "")
    group = group.replace('">P</font></font>', "")
    #group= newpage.findAll("div", {"class":"name"})
    #print species
    #group = re.match('(tle)*', str(info))
    #print group
    
    
    description = newpage.findAll("div", {"class":"description"})
    description = re.sub('<[^>]+?>', '', str(description[0]))
    sep3 = []
    #print description


    separate = description.split('\n')
    sep2 = [line for line in separate if line>0]
    for line in sep2:
        if line != '' and line[0]!=' ':
            sep3.append(line)

  
    for line in sep3:
        

        
        words = line.split(':')
        
        species = words[0]
        genes = words[1]
        holder.append([KOG, species, genes, spec, group])




f = open("KOGdictionary2.csv", "w")
w = csv.writer(f)
for line in holder:
    w.writerow(line)

f.close()
