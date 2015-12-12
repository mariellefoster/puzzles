#Euler7.py

'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 
13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def main():
	prime = 3
	num = 5
	while prime != 10002:
		if isPrime(num):
			print num
			prime += 1

		num += 2





def isPrime(num):
	for x in range(3, int(math.sqrt(num) +1)):
		if num%x == 0:
			return False
	return True

main()