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


def turnAroundtime(process, wt, tat):
	for i in range(len(process)):
		tat[i]=process[i][2]+wt[i]

def avgTime(process, quantum):
	n=len(process)
	wt=[0]*n
	tat=[0]*n
	total_wt=0
	total_tat=0

	waitingTime(process, wt, quantum)
	turnAroundtime(process, wt, tat)

	for i in range(n):
		total_wt=total_wt+wt[i]

	for i in range(n):
		total_tat=total_tat+tat[i]

	avg_wt=total_wt/n
	avg_tat=total_tat/n

	display(process, wt, tat, avg_wt, avg_tat)



def display(process, wt, tat, avg_wt, avg_tat):
	print('Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time')

	for i in range(len(process)):
		print('{}\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], wt[i], tat[i]))

	print('\nAverage Waiting Time: ', avg_wt)
	print('Average Turn Around: ', avg_tat)