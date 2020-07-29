from numpy import prod

begin_number = 2
end_number = 25
arr_colection = []
sum_value = 0
product_value = 0

for i in range(begin_number, end_number):
	result = False
	tmp = int(i**0.5)

	# While Loop is a form of Recursion
	while (tmp > 1):
		if (i%tmp == 0): result = True	
		tmp -= 1
        
	if not result: 
        	arr_colection.append(i) 

sum_value = sum(arr_colection)
product_value = prod(arr_colection)

print (f'{str(len(arr_colection))} numbers found: \n {arr_colection}')
print (f'\n the sum of the numbers: \n {sum_value}')
print (f'\n the product of the numbers: \n {product_value}')
