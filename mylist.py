import ctypes


class mylist:
    def __init__(self):
        self.size=1
        self.num=0
        #create array at the time of construct of obj
        self.A=self.__make__array(self.size)

    def __len__(self):
        return self.num

    def append(self,value):
        if self.num==self.size:
            #resize
            self.__resize(self.size*2)
          
        self.A[self.num]=value
        self.num+=1


    def __str__(self):
        #print item of list 
        result=""
        for i in range(self.num):
            result=result+str(self.A[i])+","
        return "[" + result[:-1] + "]"
    
    def __getitem__(self,index):
        if 0<= index<self.num:
          return self.A[index]
        else:
            return "ERROR-index out of bound"


    def __resize(self,new_capacity):
        #resize the capacity by 2 
        B=self.__make__array(new_capacity*2)
        #copy elements from old to new size array
        for i in range(self.num):
           B[i]=self.A[i]

        self.A=B

    def pop(self):
     #it delete the last item from list
        if self.num==0:
         return "empty list"
        
        print(self.A[self.num-1])
        self.num-=1

    def clear(self):
        self.num=0
        self.size=1

    def find(self,value):
        for i in range(self.num):
            if self.A[i]==value:
                
               return i 
        return "value-error:value is not in list"    


            


    #define make array
    def __make__array(self,capacity):
        return(capacity*ctypes.py_object)()

    

    
    
l=mylist()
l.append(1)
l.append('hellow')
l.append(4.5)
l.append(89)
print(l)
print(l[56])
print(len(l))
l.pop()
print(l)
l.pop()
print(l)