    data_changes = {
        '253036': [''], 
        '313115': ['313113']
        }

    modem_changes = {'305403': [], 
                     '311957': ['253036', '312591']
                     }

    modem_trans = {
        '311957': '12345',
        '12345':  ''
        '305403': ''
    }

    data_trans = {
        '313115':'',
        '253036':'',
        '12345':' ',
    }

    data_changes_orig = data_changes
    modem_changes_orig = modem_changes

    for k,v in data_changes.items():
        if k not in modem_changes_orig and k in modem_trans:
            modem_changes[k] = [ modem_trans[k] ]

    for k,v in modem_changes.items():
        if k not in data_changes_orig and k in data_trans:
            data_changes[k] = [ data_trans[k] ]


    >>> modem_changes
    {'311957': ['253036', '312591'], '313115': [''], '253036': [''], '305403': []}
    >>> data_changes
    {'313115': ['313113'], '253036': ['']}
    
    
    
    def data_changes_func(key):
        if key == '311957':
            output = '12345'
        if key == '12345'
            output = ''
        if key == '305403':
            output = ''
        return output
        
    for k,v in modem_changes.items():
        if k not in data_changes_orig:
            data_changes[k] = data_changes_func(key)
