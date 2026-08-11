import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print(marks)
print(np.mean(marks))
print(np.shape(marks)) #or use marks.shape
result=np.mean(marks,axis=1) #axis 1count across
print(result)
print(result.shape)
result1=np.mean(marks,axis=0) #axis 0 count downwrds
print(result1)
print(result1.shape)
print(np.median(marks))
result2=np.median(marks,axis=1)
print(result2)
print(np.median(marks))
result3=np.median(marks,axis=0)
print(result3)

print(np.std(marks))
print(np.var(marks))
