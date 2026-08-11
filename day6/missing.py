import pandas as pd
import numpy as np

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))