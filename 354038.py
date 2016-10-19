blocks = []
current = dict( lines=[] )

lines = [
'6. Subject',
'7. Something else',
'8. Some more',
]

for line in lines:
    n,remainder = line.split(l,'.',1) # Split at first . after number assuming always there
    
    try:
        int(n) # Check is a number
    except:
        if len(current['lines']) > 0:
            blocks.append(current)
            current = dict( lines=[] )

        current = dict()  # Reset
    else: # Starts with a number
        if n == 6: # Subject
            current['subject'] = remainder

        elif n >= 8: # Skip 7
            current['lines'].append( remainder )
        
if len(current['lines']) > 0:
    blocks.append(current)
    current = dict( lines=[] )
    
