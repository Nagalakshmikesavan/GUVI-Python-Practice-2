n=int(input())
m=int(input())
for i in range(n,m+1):
	for j in (2,i):
		if(i%j==0):
			break
		else:
			print(i)
