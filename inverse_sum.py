import time
start = time.time()
l=0
while(l<100000):
  n=1000
  sum1=0
  for i in range(1,n+1):
    sum1=sum1+(1/i)
  print("The sum of the series is: ",round(sum1,2))
  l=l+1
end = time.time()
print(end - start)
