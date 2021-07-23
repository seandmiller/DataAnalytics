data = [("johny",23),("charlie", 20), ("john", 40), ("charlie",100), ("sam", 23),("john", 400), ("blake", 70), ("sam", 45),("johny", 200),("natasha",20),("natasha",30)]

data=sorted(data)
#print(data)
def shrt(data):
  ls=[]
  for x in data:
    f=0
    t=0
    for y in data:
        if x[0]==y[0] and x[1]!=y[1]:
            new_tuple = (y[0],x[1]+ y[1])
            ls.append(new_tuple)
            data[data.index(x)]= (0,0)
            data[data.index(y)]= (0,0)
            t=True
        else:
            f=False
    if f==False and t != True and x!=(0,0):
        ls.append(x)
  
  return ls
  
print(shrt(data))
