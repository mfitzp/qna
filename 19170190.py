f = ['Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors',
'Erdos, P., Reisig, W.: Stuttering in petri nets',
'Smith, M.N., Chen, X.: First order derivates in structured programming',
'Jablonski, T., Hsueh, Z.: Selfstabilizing data structures']

author_en = {} # Dict to hold scores/author
coauthors = []
targets = ['Smith, M.N.','Hsueh, Z.','Chen, X.']

for line in f:
    print line
    # Split the line on the :
    authortext,papers = line.split(':')

    # Split on comma, then rejoin author (every 2)
    # See: http://stackoverflow.com/questions/9366650/string-splitting-after-every-other-comma-in-string-in-python
    authors = authortext.split(', ')
    authors = map(', '.join, zip(authors[::2], authors[1::2]))

    # Authors now contains a list of authors names    
    coauthors.append( authors )

    for author in authors:
        author_en[ author ] = None
    
author_en['Erdos, P.'] = 0 # Special case

# Now we have a list of lists: each list containing co-authors from a given publication
# and a dict to hold the scores.

for ca in coauthors:
    minima = None
    for a in ca:
        if author_en[a] != None and ( author_en[a]<minima or minima is None ): # We have a score
            minima = author_en[a]
        
    if minima != None:
        for a in ca:
            if author_en[a] == None:
                author_en[a] = minima+1 #
            
for author in targets:
    print "%s: %s" % ( author, author_en[author] )            
    