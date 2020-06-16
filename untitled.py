class roman :  
    def __init__(self, r):
        self.pow = [' ','I',"V","X",'L','C','D','M']
        self.pow2= [0,1,5,10,50,100,500,1000]
        self.ori = {}
        for i in self.pow:
            self.ori[i] = 0
        j = 0
        for i in r:
            if j==len(r)-1:
                self.ori[i] += 1
                pass
            else:
                if(self.pow.index(r[j])<self.pow.index(r[j+1])):

                    self.ori[i] -= 1
                else:
                    self.ori[i] += 1
                j+=1 
        
        
        
        self.spiral = int(self)
        
           
        a = self.bangsuan(self.spiral)
        self.tr = {}
        j = 1
        for i in a:
            self.tr[self.pow[j]]=i
            j+=1
        self.name = self.str()

        
    def __lt__(self, rhs): 
        return self.spiral<rhs.spiral
    def str(self): 
        j = 1
        st = ""
        for i in self.pow:
            if(i == ' '):
                pass
            else:
                if(self.tr[i]==-1):
                    jay = self.pow[j+1]
                    if(self.tr[jay]==0):
                        self.tr[self.pow[j+2]] -= 1
                        st = self.pow[j] +self.pow[j+2]+st
                    else:
                        self.tr[jay]-=1
                        st = self.pow[j] +self.pow[j+1]+st    
                else:
                    for p in range(self.tr[i]):
                        st = i+st
                        
                j+=1
        return st
            
    def __str__(self):
        return self.name

    def __int__(self): 
        spiral = 0
        for i in range(len(self.pow)):
            spiral += (self.ori[self.pow[i]]*self.pow2[i])
        return spiral
    def __add__(self, rhs): 
        return roman(str(self)+' '+str(rhs))
    
    def bangsuan(self,a):
        c = [1000,500,100,50,10,5,1]
        b = []
        for i in c:

            b.append(a//i)
            a = a%i
        j = 0
        b = b[::-1]
        for i in b:
            if j==6:
                break
            if(j%2==0):
                if(i>=4):
                    b[j]-=5
                    b[j+1]+=1
            else:
                if(i>=2):
                    b[j]-=2
                    b[j+1]+=1
            
            j+=1
        return b
t, r1, r2 = input().split()
a = roman(r1);b = roman(r2)
if   t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else          : print(str(a + b))
        

