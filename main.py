import random

def swap(a,i,j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp
  
def partition(a,l,r,p_index):
  p = a[p_index]
  swap(a,l,p_index)
  i = l+1
  for j in range(l+1,r+1):
    if(a[j] < p):
      swap(a, i, j)
      i+=1
  swap(a,l,i-1)
  return a.index(p)

def rselect(a,l,r,i):
  n = r-l
  if (n==1): return a[l]
  p = random.randint(l,r)
  val = a[p]
  j = partition(a,l,r,p)
  if(i==j): return val
  if (j>i): return rselect(a,l,j-1,i)
  if (j<i): return rselect(a,j+1,r,i-j)

a=[5,7,2,4,1,3]
print(rselect(a,0,len(a)-1,1))