#INCLUDE:
#FILE: example_3.py

import pandas as pd;
df = pd.DataFrame({ "numbers": range(1,10) } )
df.head()
df.plot()