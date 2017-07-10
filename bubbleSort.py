#bubble sort

#input Array
A = [1,5,2,7,8,10,4,3,6,9]

sorted = False

while( sorted == False):
    
    sorted = True
    for i in range(0,len(A)-1):
        if( A[i] > A[i+1] ):
            sorted = False
            temp=A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            

#sorted output array
print('Sorted A = \n')
print(A)
