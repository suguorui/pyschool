def generateNumber(start,end,step): 
	t=range(start, end, step)
	if start<end:
		if (t[-1]+step)>end:
			z=range(start,end,step)
		else:
			z=range(start,end,step)
			z.append(end)
	elif start==end:
		z=end
	else:
		z=range(start,end,step)
	return z
