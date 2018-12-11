import time
start = time.time()
l=0
while(l<100000):
  n=1
  while(n<13):
    i=n
    p=1
    while(i>0):
      p=p*i
      i=i-1
    print("The factorial is: ",p)
    n=n+1
  l=l+1
end = time.time()
print(end - start)
