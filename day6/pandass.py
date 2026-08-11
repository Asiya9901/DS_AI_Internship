import pandas as pd
import numpy as np
x=[1,2,3,4]
y=pd.Series(x)
print(y)




x1=np.array([2,3,4])
y1=pd.Series(x1)
print(y1.to_string()) #to remove default dtype printed in output


x3={'math':80,"science":50,'hindi':90}    #dict
y3=pd.Series(x3)
print(y3.to_string())
print(y3[y3>50])
print(y3.index[0])



s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c']) #chnges the default index 0,1... to specified index a,b....
print(s1)
print(s2)
print(s2.index.to_list()) #to print only index in output


marks=pd.Series([85,90,78],index=['math','phy','chem'])
print(marks['math'])
print(marks[['math','chem']])




scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed.to_string())