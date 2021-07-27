# Initialize all men and women to free (in here I use True for being free)
# My inputs are dictionaries (men, women) in here and 
# number of men = number of women = n = 4 in this example

men = {'A': True, 'B': True, 'C': True, 'D': True}
women = {'J': True, 'K': True, 'L': True, 'M': True}

# At the end, I want such a match
match = {'A': 'K', 'B': 'L', 'C': 'J', 'D': 'M'}


# key, value
for man, freeM in men.items():
    if freeM == True:
        for woman, freeW in women.items():
            if freeW == True: 
                if(match.get(man) == woman):
                    print( man, ' and ', woman, ' become engaged.' )
                    freeM == False
                    freeW == False
        

    
    
    
