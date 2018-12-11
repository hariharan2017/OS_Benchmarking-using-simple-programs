import time
start = time.time()

l=0
while(l<100000):
  n=0
  while(n<15):
    t1=n
    t2=n*n
    t3=n*n*n
    t4=n*n*n*n
    t5=n*n*n*n*n
    sm=t1+t2+t3+t4+t5
    print("The sum is: ",sm)
    n=n+1
  l=l+1

end = time.time()
print(end - start)
