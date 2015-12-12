#Euler5.py

'''
2520 is the smallest number 
that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?

'''

num = 1
for i in range(2,21):
	if num%i != 0:
		print num
		for j in range(2,21):
			tryy = num*j
			print tryy
			if tryy%i == 0:
				num = tryy
				#print tryy
				break

print num