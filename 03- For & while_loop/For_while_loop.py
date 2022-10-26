'''
for x in [1,2,3,4,5,6,7,8,9,10]:
  print(x)  

print('----------------------------------------')

for x in [[5,6,7,8],1,2,3,4,5,6,7,8,9,10]:
  print(x)  


print('----------------------------------------')


for x in 'python':
  print(x)


print('----------------------------------------')


for x in range (0,11):
  print(x)  


for x in range (0,101,2):
  print(x)  

list(range(2,10))


for x in range (5):
    for y in range (3):
        print(x,y)



for x in range (1,11):
    for y in range (1,13):
        print (f"{x} X {y} = {x*y}")
    print('----------------------------------------')



x = 0

while x < 5 :
  y = 0
  while y < 10 :
    print(x,y)
    y += 1
  x += 1


print('----------------------------------------')

for x in range(10):
  if x == 5 :
    continue
  print(x)

for x in range(10):
  if x == 5 :
    break
  print(x)


for x in range(1,100):
  if x%2 != 0 :
    continue
  print(x)
print("Done")  

'''

'''
start = int(input("Enter start : "))
end   = int(input("Enter end : "))

print("Number \t Square")
print('----------------------------')

for x in range(start,end+1):
  print(x,'\t',x*x)
'''


'''
row = int(input("Enter row : "))
cols   = int(input("Enter cols : "))

for x in range(row):
  for y in range(cols):
    print('*', end = '')
  print('')
  
'''

for x in range(8):
  for y in range(x+1):
    print('*', end = '')
  print('')
  





