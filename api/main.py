# this is for api "Backend"
def waitingTime(process, wt, quantum):
	n=len(process)
	rt=[0]*n

	for i in range(n):
		rt[i]=process[i][2]

	current_t=0

	while(1):
		flag=True	

		for i in range(n):
			if rt[i]>0:
				flag=False

				if rt[i]>quantum:
					current_t+=quantum
					rt[i]-=quantum

				current_t+=rt[i]
				wt[i]=current_t-process[i][2]
				rt[i]=0

		if flag==True:
			break