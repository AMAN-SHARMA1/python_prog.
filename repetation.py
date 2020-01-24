a=input()
b=''
for i in a:
	if i not in b:
		c=a.count(i)
		print(i,':',c)
		b+=i
