#Question

# On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. 
#One power of the Qux is that if two of them are standing next to each other, 
#they can transform into a single creature of the third color.

# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |


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

		
