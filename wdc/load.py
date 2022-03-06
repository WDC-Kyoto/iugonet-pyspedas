


from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from config import CONFIG


# iugonet.wdc.load.qddays

def qddays(trange):
	### get remote path ###
	file_names = dailynames(trange=trange, file_format='%Y',
													prefix='qd', directory='data/day/qddays/')
	### download file ###
	local_files = download(remote_file=file_names, 
									       remote_path=CONFIG['remote_data_dir_qddays'], 
									       local_path=CONFIG['local_data_dir_qddays'], 
									       last_version=True)
	return local_files    




### iugonet.wdc.load.wp_index

def wp_index(trange=['2011-01-01', '2011-01-03']):
	### get remote path ###
	directory  = dailynames(trange=trange, file_format='%Y%m%d')
	file_names = dailynames(trange=trange,file_format='%Y%m%d',prefix='index_', suffix='.html')

	### download file ###
	local_path = [CONFIG['local_data_dir_wp_index'] + '/' + dire[0:6] for dire in directory]
	remote_path = [CONFIG['remote_data_dir_wp_index']  + dire[0:6] + '/' for dire in directory]

	local_files = []
	for i in range(len(file_names)) :
		lf = download(remote_file=file_names[i],
		    			  	 remote_path=remote_path[i],
							 	   local_path=local_path[i]) 
		local_files.append(str(lf[0]))
	return local_files
	
  



