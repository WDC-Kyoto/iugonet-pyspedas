

import load

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


print(qddays())

