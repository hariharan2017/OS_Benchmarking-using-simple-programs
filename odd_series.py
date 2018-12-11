import time
start = time.time()
l=0
while(l<10000):
  lower=1
  upper=1000
  for i in range(lower,upper):
    if(i%2!=0):
      print(i," ")
  l=l+1
end = time.time()
print(end - start)
