salary=int(input("enter salary:"))
year=int (input("enter the year"))
if year>10:
  print (salary*0.1)
if year>=6 and year<=10:
  print(salary*0.08)
else:
  print(salary*0.06)