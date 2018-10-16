x=int(input())
y=""
while(x!=0):
    y=y+' '+str(x%10)
    x=x//10
print(y[::-1])
