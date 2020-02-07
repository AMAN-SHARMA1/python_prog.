t8=(5,78,64,23,5,90,78)
t=[]
for i in t8:
	if t8.count(i)>1:
		if i not in t:
			t.append(i)
print(t)
