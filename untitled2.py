import numpy as np 
 
def mult_table(nrows, ncols):    # คนือาเรยท์มี่ ีshape เป็น (nrow, ncols) ภายในเก็บตารางสตูรคณู (ดตูัวอย่างขา้งลา่ง) 
    a = []
    for i in range(nrows):
        b = []
        for j in range(ncols):
            b.append((j+1)*(i+1))
        a.append(b)    
    a = np.array(a)
    return a
 
 
exec(input().strip())    