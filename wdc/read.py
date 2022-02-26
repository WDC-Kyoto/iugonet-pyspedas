

import download
from html.parser import HTMLParser



### qddays ###
def qddays(trange=['2011-1-1', '2011-1-1']):
	#
	local_files = download.qddays(trange)
  #
	yr   = []
	mon  = []
	q1   = []
	q2   = []
	q3   = []
	q4   = []
	q5   = []
	q6   = []
	q7   = []
	q8   = []
	q9   = []
	q0   = []
	d1   = []
	d2   = []
	d3   = []
	d4   = []    
	d5   = []    

	for lf in local_files :
		with open(lf) as f :
			data = f.readlines()
			# delete "\n"
			data = [d.replace('\n', '') for d in data] 
			for i in range(len(data)) :
				data0 = data[i]
				yr.append(data0[0:4])
				mon.append(data0[5:7])
				q1.append(data0[8:10]) 
				q2.append(data0[10:12]) 
				q3.append(data0[12:14]) 
				q4.append(data0[14:16]) 
				q5.append(data0[16:18]) 
				q6.append(data0[19:21]) 
				q7.append(data0[21:23]) 
				q8.append(data0[23:25]) 
				q9.append(data0[25:27]) 
				q0.append(data0[27:29]) 
				d1.append(data0[30:32])
				d2.append(data0[32:34])
				d3.append(data0[34:36])
				d4.append(data0[36:38])
				d5.append(data0[38:40])  
				
	return 0



### wp_index ###
def wp_index(trange=['2011-1-1', '2011-1-2']):
	#
	local_files = download.wp_index(trange)
	for lf in local_files:
		with open(lf) as f:
			d = f.read()

	return 0


a = qddays()




			
