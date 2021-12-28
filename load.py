


from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from config import CONFIG


# iugonet.wdc.qddays

def qddays(trange):
	### get remote path ###
	print(trange)

	file_names = dailynames(trange=trange, file_format='%Y',\
													prefix='qd', directory='data/day/qddays/')
	### download file ###
	local_files = download(remote_file=file_names, \
									 remote_path=CONFIG['remote_data_dir'], \
									 local_path=CONFIG['local_data_dir'], \
									 last_version=True)
	return local_files    







