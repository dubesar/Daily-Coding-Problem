#Qustion

# Given two strings A and B of lowercase letters, return true if and only if
#we can swap two letters in A so that the result equals B.

# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false


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
