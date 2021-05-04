a=1
b=1

fibonacci=[a,b]

for i in range(55):
  a,b=b,a+b
  fibonacci.append(b)
print(fibonacci)