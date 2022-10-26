

# 2 Numbers To print the numbers between them
print("choose 2 Numbers To print the numbers between them ")
x = int(input(' Enter First Number : '))
y   = int(input(' Enter Second Number : '))
for n in range(x+1,y):
    print(n)
    

 

# number from 0 to 100 that can be divided by this

print(" welcome , choose one number ...")                
x = int(input(' Enter First Number : '))
for n in range(1,101):
  if n%x == 0 :    
   print(n)
