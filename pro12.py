n=int(raw_input())
if(n>1):
	for x in range(2,n):
		if (n%x == 0):
			print("no")
			
			break
	else:
		print("prime")

		
