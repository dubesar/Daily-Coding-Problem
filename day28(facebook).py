arr = list(map(str,input().split()))
stack = [arr[0]]
while len(set(arr))!=1:
	for i in range(1,len(arr)):
		if stack[-1]!=arr[i]:
			if stack[-1]=='R' and arr[i]=='B':
				stack[-1]='G'
			elif stack[-1]=='G' and arr[i]=='B':
				stack[-1]='R'
			elif stack[-1]=='R' and arr[i]=='G':
				stack[-1]='B'
			elif stack[-1]=='B' and arr[i]=='G':
				stack[-1]='R'
			elif stack[-1]=='G' and arr[i]=='R':
				stack[-1]='B'
			elif stack[-1]=='B' and arr[i]=='R':
				stack[-1]='G'
		else:
			stack.append(arr[i])
	arr = stack
	stack = [arr[0]]
print(stack)

		
