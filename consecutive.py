import numpy as np
list_=[1,1,1]
consecutive=[]
def count(list_,start):
    count=0
    j=start
    while j<len(list_) and list_[j] ==1:
        count+=1
        j=j+1   
    return count,(start+count-1)
i=0
while i<len(list_):
    if list_[i]==1:
        countval,update=count(list_,i)
        i+=update
        consecutive.append(countval)
    else:
        i+=1    
        
try:
    min_=min(consecutive)
    max_=max(consecutive)
    print(min_,max_)
except:
    print('0,0')
