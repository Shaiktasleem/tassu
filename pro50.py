def isPowerOfTwo (t):
	return (t and (not(t & (t-1))))
N=int(input())
if(isPowerOfTwo(N)):
	print("yes")
else:
	print("no")
