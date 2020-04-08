a = list(input())
b = list(input())

flag = 0
for i in range(len(a)-1):
	if a[i]!=b[i]:
		if b[i+1]==a[i] and a[i+1]==b[i]:
			flag+=1
if flag>1 or flag<1:
	print('false')
else:
	print('true')
