#Euler 4

'''
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def main():
		
	maxx = 999
	minn = 100
	maxpalindrome = 0
	for x in range(minn, maxx +1):
		for y in range(minn, maxx +1):
			tryy = x*y
			if isPalindrome(tryy) and tryy > maxpalindrome:
				maxpalindrome = tryy

	

	print maxpalindrome

def isPalindrome(num):
	test = str(num)
	return test == test[::-1]

main()