import time
start = time.time()
l=0
while(l<1000):
  r=1000
  for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
      if(a%i==0):
        k=k+1
    if(k==0):
      print(a," ")
  l=l+1
end = time.time()
print(end - start)
