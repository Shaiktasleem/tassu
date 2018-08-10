n,k=map(int,raw_input().split())
list=[int(i) for i in raw_input().split()]
s=0
for x in range(0,k):
	s+=list[x]
print(s)
