t5=()
while 1:
	item=input('enter your item')
	t5=t5+(item,)
	i=input('want to add more y/n')
	if i.lower()=='n':
		break
print(t5)

