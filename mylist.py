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
        #it clear the value of list completely
        self.num=0
        self.size=1

    def find(self,value):
        #it find the value's index
        for i in range(self.num):
            if self.A[i]==value:
                
               return i 
        return "value-error:value is not in list"    


    def insert(self,pos,value):
        #if there is no vacant space after last index then we increase size 
        if self.num==self.size:
            self.__resize(self.size*2)
        # let start the loop from last to pos+1 here pos is pos+1 in indexing form
        for i in range(self.num,pos,-1):
            self.A[i+1] = self.A[i]
        #put that value in required index and increase self.num by 1
            
        self.A[pos]=value
        self.num+=1

    def __delitem__(self,pos):
        if 0<=pos<self.num:
         for i in range(pos,self.num-1):
            self.A[i]=self.A[i+1]
         self.num-=1
        else:
            print( "index is not available")
    
    def remove(self,value):
        pos=self.find(value)

        if type(pos)== int:
            #delete
            self.__delitem__(pos)
        else:
            return pos
            

    

    #define make array
    def __make__array(self,capacity):
        return(capacity*ctypes.py_object)()

    

    
    
l=mylist()
l.append(1)
l.append(2)
l.append('hello')
l.append(4.5)
print(l)
l.remove(2)
print(l)




