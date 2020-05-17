import math

def is_prime(n):
	if n<2:
		return False
	else:
		for i in range(2,int(math.sqrt(n)+1)):
			if(n%i==0):
				#print(f"{n} is not a prime number")
				return False
		#print(f"{n} is a prime number")
		return True
			
