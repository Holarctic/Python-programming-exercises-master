def fact(x):
	if(x == 0):
		return 1
	ans = x
	for i in range (2, x):
		ans *= i
	return ans
x = int(raw_input())
print fact(x)
