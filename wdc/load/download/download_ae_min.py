

from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from .config import CONFIG



def download_ae_min(trange, level='provisional') :

    inames = ['ae', 'al', 'au', 'ao']

    ### real time
    if level == 'real_time' :
        pass



    ### provisional
    if level == 'provisional' :

        directory = CONFIG['remote_data_dir_ae'] + 'min/index/'

        ## get remote path
        year = dailynames(trange=trange, file_format='%Y%m')
        year = [ yr[0:4] for yr in year ]*4

        remote_file = []
        for iname in inames :
            remote_file += dailynames(trange=trange, file_format='%y%m', prefix=iname)

        remote_file = [ directory + yr + '/' + rf for (yr, rf) in zip(year, remote_file) ]

        i = 0
        for (rf, yr) in zip(remote_file, year) :
            if int(yr) < 1996 :
                subdir = rf[-6] + '.' + rf[-5]  # ae -> a.e
                remote_file[i] = rf.replace('index/', 'index/'+ subdir + '/') 
            if int(yr) >= 1996 :
                remote_file[i] = rf.replace('index/', 'index/pvae/')
            i += 1


        ## download
        local_path = CONFIG['local_data_dir_ae'] + '/min/'
        local_path = [ local_path + yr for yr in year ]
        local_file = []
        for (lp, rf) in zip(local_path, remote_file) :
            f = download(remote_file=rf, local_path = lp)
            if f :
                local_file.append(f[0])



    ### final
    if level == 'final' :
        pass



    return local_file

