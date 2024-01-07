from  math import cos

x1=100

while(True):

  x2=cos(x1)
  print(x2-x1)
  if(abs(round((x2-x1),3))<0.001):
      print("Root is ", x1)
      break
  else:
      x1=x2
    
