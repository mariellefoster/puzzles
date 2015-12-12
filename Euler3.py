#project Euler #3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math


def main():
	biggestPrime = 3
	num = 600851475143
	current = 3
	while current < int(math.sqrt(num)):
		if isPrime(current):
			if num%current == 0:
				biggestPrime = current
		current += 2
	print biggestPrime

def isPrime(num):
	for x in range(3, int(math.sqrt(num))):
		if num%x == 0:
			return False
	return True

main()