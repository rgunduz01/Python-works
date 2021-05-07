def parrot_trouble(talking, hour):
  if hour in range(1,24):
   return talking==True and (hour<7 or hour>20)
  else:
    print("Not in range")