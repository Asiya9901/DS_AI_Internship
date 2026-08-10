import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.mean())


marks=[10,20,30]
new_marks=[]
for x in marks:
    new_marks.append(x+5)

print(new_marks)



import numpy as np
marks=np.array([10,20,30])
results=marks+5
print(results)



import numpy as np
x=np.array([[10,20,30],
           [40,50,60],
           [70,80,90]])
y=np.array([[5],[10],[5]])
print(x+y)



import numpy as np
x=np.array([[2,1,1],[2,1,3]])
print(x.reshape(3,2))
print(x.flatten())
print(x.transpose())



a=np.array([1,2])
b=np.array([3,4])
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.concatenate(x))
print(np.concatenate((a,b),axis=0))


