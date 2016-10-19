import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.DataFrame({
               "GEO": [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3],
               "year": [2010,2011,2010,2011,2010,2011,2010,2011,2010,2011,2010,2011,2010,2011,2010,2011,2010,2011],
               "GROUP": ['doctor','doctor','Knight','Knight','Wizard','Wizard','doctor','doctor','Knight','Knight','Wizard','Wizard','doctor','doctor','Knight','Knight','Wizard','Wizard'], 
                "Value": random.sample(xrange(100), 18)
})

provs = df["GEO"].unique()
f, axarr = plt.subplots(len(provs), sharex=True, sharey=True)
myplot = 0

for prov in provs:
    groups = df.loc[df["GEO"] == prov, "GROUP"].unique()
    axarr[myplot].set_title(prov)
    for group in groups:
        x = df.loc[(df["GEO"] == prov) & (df["GROUP"] == group), "year"].tolist()
        y = df.loc[(df["GEO"] == prov) & (df["GROUP"] == group), "Value"].tolist()

        axarr[myplot].ticklabel_format(style='plain', useOffset=False)
        axarr[myplot].plot(x, y, label=group)    
        axarr[myplot].set_ylabel('Amount in $')
        axarr[myplot].set_xticks([2010, 2011])

    myplot = myplot + 1


plt.xlabel('Year')  # Only on the final plot (bottom)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()