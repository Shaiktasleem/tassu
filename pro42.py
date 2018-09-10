x1,x2=map(str,raw_input().split())
l1=len(x1)
l2=len(x2)
if l1==l2:
	if x1==x2:
		print x1
	elif x1>x2:
		print x1
	else:
		print x2
elif l1>l2:
	print x1
else:
	print x2
