#!/usr/bin/python
# Reid Stuberg
# Programming Assignment 3
# 5/22/2017
#

from random import randrange
from random import randint
import operator

def printtrigrams(files):
    dictionary = {}
    words = ""
    for element in range(len(files)):
        for i in range(len(files[element])):
            line = files[element][i]
            line = line.strip()
            x = tuple(line.split(' '))
            #parsing
            if (len(x) >= 1): 
                for j in range(len(x)-2) :
                    s0 = x[j].lower()
                    s1 = x[j+1].lower()
                    s2 = x[j+2].lower()
                    #no random ''
                    if (len(x[j+1]) >= 1 and len(x[j+2]) >= 1):
                        # does the thing not exist?
                        if (dictionary.has_key(s0)):  
                            if (dictionary[s0].has_key(s1)):
                                #nested dic? 
                                if ( dictionary[s0][s1].has_key(s2) ): 
                                    #found this item again
                                    dictionary[s0][s1][s2] += 1
                                else:
                                    #new key for third val
                                    dictionary[s0][s1].update({s2:1})
                            else :
                                #new key for 2nd val
                                dictionary[s0].update({s1: {s2:1}})
                        else:
                            # new field
                            dictionary.update({s0: {s1: {s2:1}}})
    #dictionaries now contain trigrams                

    #choose a random first element
    pick = dictionary.keys()
    this = pick[randrange(0, len(pick))]

    #print 1000 line story
    for i in range(500):
        selected = []
        l1 = {}
        #there are cases where third trigram word is not found as the first word
        try:
            l1 = dictionary[this].keys()
        except KeyError:
            this = pick[randrange(0, len(pick))]
            l1 = dictionary[this].keys()
        for bi in range(len(l1)):
            #highest chain prob          
            maxs = 0
            l2 = dictionary[this][l1[bi]].keys()
            for tri in range(len(l2)):
                #find highest prob and add total
                maxs +=  dictionary[this][l1[bi]][str(l2[tri])]
            selected.append(maxs)
            if ( bi == len(l1)-1):
                random_index = randrange(0, len(selected))
                n1 = l1[random_index]
                high = 0
                piv = -1
                l2 = dictionary[this][n1].keys()
                for lk in range(len(l2)):
                    if (high < int(dictionary[this][n1][l2[lk]])):
                        high = int(dictionary[this][n1][l2[lk]])
                        piv = lk
                words = words + " " + n1 + " " + l2[lk]
                this = l2[lk]
    print words
    return
#printtrigram()

def main():
    # text names
    b1 = "doyle-case-27.txt"
    b2 = "alice-27.txt"
    b3 = "twain-adventures-27.txt"
    b4 = "doyle-27.txt"
    b5 = "london-call-27.txt"
    b6 = "melville-billy-27.txt"
    #Read each file
    inf1 = open(str(b1),"r")
    text1 = inf1.readlines()
    inf1.close()
    inf2 = open(str(b2),"r")
    text2 = inf2.readlines()
    inf2.close()
    inf3 = open(str(b3),"r")
    text3 = inf3.readlines()
    inf3.close()
    inf4 = open(str(b4),"r")
    text4 = inf4.readlines()
    inf4.close()
    inf5 = open(str(b5),"r")
    text5 = inf5.readlines()
    inf5.close()
    inf6 = open(str(b6),"r")
    text6 = inf6.readlines()
    inf6.close()
    filelist = []
    filelist.append(text1)
    filelist.append(text2)
    filelist.append(text3)
    filelist.append(text4)
    filelist.append(text5)
    filelist.append(text6)
    #print story based on file list function
    printtrigrams(filelist)

main()
#end program
