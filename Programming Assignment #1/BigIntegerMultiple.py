# Big Integer Mutiply
# Simple we change x*y into (a+b)+(c+d) and also use Galss's method to change the effiency
# T(n) = 4T(n/2)+O(1)
# T(n) = 3T(n/2)+O(1)
# limitation: the digit of each number should be the same

def BigIntegerMutiple(x,y):
	# count on the digit
	i = 0
	x_ = x
	while x_>0:
		x_ = x_//10
		i = i + 1
	if i > 1:
		return x*y
	else:
		a = x//(pow(10,i//2))
		b = x%(pow(10,i//2))
		c = y//(pow(10,i//2))
		d = y%(pow(10,i//2))
		ac = BigIntegerMutiple(a,c)
		bd = BigIntegerMutiple(b,d)
		bcad = BigIntegerMutiple(a+b,c+d)
		print("ac is :",ac)
		print("bd is :",bd)
		result = pow(10,i)*ac + bd + pow(10,i//2)*(bcad-ac-bd)
		return result

print(BigIntegerMutiple(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))