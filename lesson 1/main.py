import numpy as np

list1=[9,1,63,8,23]
print(type(list1))



sampleArray=np.array(list1)
print(type(sampleArray))




#array2=np.array([1,2,3],'hello')
#print(type(array2))

array0=np.zeros(7)
print(array0)

array1=np.ones(2)
print(array1)

floatArray=np.array(list1,dtype='f')
print(floatArray)

array2dv1=np.array([[2,6],[40,79]])
array2dv2=np.array([[2,6,7,8,40],list1])
print(array2dv1)
print(array2dv2)


print(array0.ndim)
print(array0.shape)
print(array2dv2.shape)
print(array2dv2.size)

print(array0.nbytes)
print(array2dv2.nbytes)


numArray=np.arange(1,109)
print(numArray)

oddArray=np.arange(5,100,5)
print(oddArray)

randomArray=np.random.permutation(numArray)
print(randomArray)

reshapeNumAray=numArray.reshape(27,4)
print(reshapeNumAray)


sortedArray=np.sort(floatArray)
print(sortedArray)





