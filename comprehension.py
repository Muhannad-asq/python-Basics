
numbers = [1,2,3,4,5,6,7,8,9,10]

new_numbers = []

for n in numbers :
    new_numbers.append(n*n)


print(new_numbers)


new_number2 =[n*n for n in numbers]
    
print(new_number2)



new_number3 = [n*m for n in range(1,3) for m in range (1,5)]

print(new_number3)



evene = [n for n in range (1,101) if n%2 == 0  ]

print(evene)

