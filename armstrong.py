while True:

  num=(input("Enter a number.If you want to exit, type q:"))
  if num=='q':
   break


  uzunluk=len(num)
  summ=0
  for i in range(uzunluk):
   summ = summ + int(num[i])**uzunluk
  if (num==uzunluk):
      print("Armstrong number!")
  else:
      print("Not Armstrong number!")