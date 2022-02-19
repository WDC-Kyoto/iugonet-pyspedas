from pyspedas.utilities.dailynames import dailynames
from pyspedas.utilities.download   import download
from config import CONFIG
import os
CONFIG={'local_data_dir_wdc':'iugonet/wdc_kyoto/geomag/','remote_data_dir_wdc':'http://wdc-data.iugonet.org/data/'}
def ae(trange,level,res):
    #[['min/index/ae/2013/ae.1203/']が正しい形や！
    out_files = []
    dir_wdc=[]
    prefix=[]
    if(level=='all' or level=='final'):
        dir_wdc.extend([res+'/index/ae/',res+'/index/au/',res+'/index/al/',res+'/index/ao/'])
        prefix.extend(['ae.','au.','al.','ao.'])
    if(level=='all' or level[0:4]=='prov'):
        if(res=='min'):
                #before1996
            dir_wdc.extend([res+'/index/a.e/',res+'/index/a.u/',res+'/index/a.l/',res+'/index/a.o/'])
            prefix.extend(['ae.','au.','al.','ao.'])
                #after1995
            dir_wdc.extend([res+'/index/pvae/']*5)
            prefix.extend(['ae','au','al','ao','ax'])
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])

        out_files.append(local_files)

    out_files = sorted(out_files)
    return out_files
#def dst(trange,level):
#[hour/index/pvdst/2012/dst1203]

def aym(trange,level,res):
    #http://wdc-data.iugonet.org/data/min/index/asy/2012/asy1203.wdc
    out_files = []
    file_names=dailynames(trange=trange,file_format='%y%m',prefix='asy', directory='min/index/asy/2012/',suffix='.wdc')
    local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])

    out_files.append(local_files)

    out_files = sorted(out_files)
#def sym(trange,level,res):
    #: http://wdc-data.iugonet.org/data/min/index/asy/2012/asy1203.wdc
#def site(trange,site,res):
    #http://wdc-data.iugonet.org/data/hour/aae/2012/aae1203
