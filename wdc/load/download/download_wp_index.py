
 
import os
from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from .config import CONFIG




def wp_index(trange=['2011-01-01', '2011-01-01']):

    ### get remote path ###
    directory   = dailynames(trange=trange,file_format='%Y%m%d')
    remote_file = dailynames(trange=trange,file_format='%Y%m%d',prefix='index_', suffix='.html')



    ### download file ###
    local_path  = [CONFIG['local_data_dir_wp_index'] + '/' + dire[0:6] for dire in directory]
    remote_path = [CONFIG['remote_data_dir_wp_index']  + dire[0:6] + '/' for dire in directory]

    local_files = []
    for i in range(len(remote_file)) :
        lf = download(remote_file=remote_file[i],remote_path=remote_path[i],
                      local_path=local_path[i])
        
        if lf:
        local_files.append(lf[0])



    ### html to text
    for lf in local_files :
        with open(lf) as f :
            lines = f.readlines()
            l1 = [i for i, st in enumerate(lines) if '<pre>' in st]
            l2 = [i for i, st in enumerate(lines) if '</pre>' in st]
            lines = lines[l1[0]+1:l2[0]]
        with open(lf, 'w') as f :
            f.writelines(lines)
    


    return local_files



