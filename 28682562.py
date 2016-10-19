import re
import pandas 
import warnings
from pandas.io.common import DtypeWarning

myfile = '28682562.txt'
target_type = str

with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter("always")

    mydata = pandas.read_csv(myfile, sep=",", header=None)
    print("Warnings raised:", ws)
    # We have an error on specific columns, try and load them as string
    for w in ws:
        s = str(w.message)
        print("Warning message:", s)
        match = re.search(r"Columns \(([0-9,]+)\) have mixed types\.", s)
        if match:
            columns = match.group(1).split(',') # Get columns as a list
            columns = [int(c) for c in columns]
            
            print("Applying %s dtype to columns:" % target_type, columns)
            mydata.iloc[:,columns] = mydata.iloc[:,columns].astype(target_type)
            
