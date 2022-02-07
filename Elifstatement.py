chemistry=int(input("enter the chemistry score:"))
maths=int(input("enter the maths score:"))
english=int(input("enter the english score:"))
history=int(input("enter the history score:"))
biology=int(input("enter the biiology score:"))
score=(chemistry+maths+english+history+biology)/5
print('mean score:',score)
if score >=70 and score <=100:
  print('A')
elif score >=60 and score <=69:
  print('B')
elif score >=50 and score <=59:
  print('C')
  
elif score >=40 and score <=49:
  print('D')
elif score >=0 and score <=39:
  print('Fail')
else :
  print("invalid marks")