import time
start = time.time()

l=0
while(l<100000):
  nterms = 25
  n1 = 0
  n2 = 1
  count = 0

  if nterms <= 0:
    print("Please enter a positive integer")
  elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
  else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
      print(n1," ")
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
  l=l+1

end = time.time()
print(end-start)
