

import load
from html.parser import HTMLParser



### qddays ###
def qddays(trange=['2011-1-1', '2013-1-1']):
	#
	local_files = load.qddays(trange)
  #
	
	for lf in local_files:
		with open(lf) as f:
			line = f.readline()
			while line:
				line = line.rstrip()
				print(line)
				line = f.readline()
	return 0



### wp_index ###
def wp_index(trange=['2011-1-1', '2011-1-2']):
	#
	local_files = load.wp_index(trange)
	for lf in local_files:
		with open(lf) as f:
			d = f.read()

	return 0


a = wp_index()
			
