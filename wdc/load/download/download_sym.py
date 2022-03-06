


	
  
from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from .config import CONFIG
 


# iugonet.wdc.download.qddays
def sym(trange=['2011-01-01', '2011-03-01']):

    ### local
    subdir = dailynames(trange=trange, file_format='%Y%m')
    local_path  = [ os.sep.join([CONFIG['local_data_dir_sym'], sd[0:4]]) for sd in subdir ]



    ### remote
    #
    remote_path = dailynames(trange=trange, file_format='%Y%m', 
	                     directory=CONFIG['remote_data_dir_sym'])
    remote_path = [rp[:-2] for rp in remote_path]              # /YYYYMM -> /YYYY
    #
    remote_file = dailynames(trange=trange, file_format='%Y%m', 
	                     prefix='asy', suffix='.wdc')
    remote_file = [rf[0:3]+rf[5:13] for rf in remote_file]     # asyYYYYMM.wdc -> asyYYMM.wdc



    ### download
    local_file  = [ os.sep.join([local_path[i], remote_file[i]]) for i in range(len(local_path)) ]
    remote_file = [ remote_path[i]+ '/' + remote_file[i] for i in range(len(remote_path)) ]

    out_files = []
    for (rf, lf) in zip(remote_file, local_file) :
        f = download(remote_file=rf, local_file=lf)
        if f:
            out_files.append(f[0])
    

    return out_files





def asy(trange=['2011-01-01', '2011-03-01']):
    return sym(trange=trange)








