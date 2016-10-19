import re
import numpy as np

filename = "28651896.txt"

# [e] 14957596088
match_line_re = re.compile(r"^\[([a-z])\]\W(\d*)")

result = {
    'b':[],
    'd':[],
    }
    
tally_empty = dict( zip( result.keys(), [np.nan] * len(result) ) )

tally = tally_empty
with open(filename, 'r') as f:
    for line in f:
        if line.startswith('[END SECTION'):
            # Write accumulated data to the lists
            for k, v in tally.items():
                result[k].append(v)
                
            tally = tally_empty 
                   
        else:
            # Map the items using regex
            m = match_line_re.search(line)
            if m:
                k, v = m.group(1), m.group(2)
                print(k,v)
                if k in tally:
                    tally[k] = v

b = np.array(result['b'])
d = np.array(result['d'])
