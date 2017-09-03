while True:
  feet = int(input("how many feet?"))
  
  inches = 12
  
  convert = feet * inches
  
  answer = "you have %s inches for %s feet" % (convert, feet,)
  
  print(answer)