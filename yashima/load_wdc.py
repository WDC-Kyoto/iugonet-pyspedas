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
def dst(trange,level):
    """
    trange= (Optional) Time range of interest  (2 element array), if
         this is not set, the default is to prompt the user. Note
          that if the input time range is not a full month, a full
          month's data is loaded.
          fomat is trange=["yyyy-mm-dd"] ex:trange=["2012-04-05","2012-04-15"]

  level = The level of the data, the default is 'final' for geomag data.
          For AE and Dst index, the default is ['final', 'provsional'].
    """
    out_files = []
    dir_wdc=[]
    prefix=[]
#[hour/index/pvdst/2012/dst1203]
    res='hour'
    if(level=='all' or level=='final'):
        dir_wdc.append(res+'/index/dst/')
        prefix.append("dst")
    if(level=='all' or level[0:4]=='prov'):
        dir_wdc.append(res+'/index/pvdst/')
        prefix.append("dst")
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])

        out_files.append(local_files)
def aym(trange,res):
    #resにはminかhourしか入らないようにエラーメッセージ出したほうがいいかも（minデータしかない？？）
    #levelもつけておいて無視の方がエラー少なくなるかも,level=Falseを初期値で与える？
    #http://wdc-data.iugonet.org/data/min/index/asy/2012/asy1203.wdc
    out_files = []
    dir_wdc=res+'/index/asy/'
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc,suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix='asy', directory=dir_2[0],suffix='.wdc')
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        out_files.append(local_files)
    out_files = sorted(out_files)
    return out_files
def sym(trange,res):
    out_files = []
    dir_wdc=res+'/index/asy/'
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc,suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix='asy', directory=dir_2[0],suffix='.wdc')
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        out_files.append(local_files)
    out_files = sorted(out_files)
    return out_files
    #: http://wdc-data.iugonet.org/data/min/index/asy/2012/asy1203.wdc
def site(trange,site,res):
    #http://wdc-data.iugonet.org/data/hour/aae/2012/aae1203
    #siteの文字を分けて取り出すのがまだ。
    out_files = []
    dir_wdc=[]
    prefix=[]
    suffix=[]
    dir_wdc.append(res+'/'+site.lower()+'/')
    prefix.append(site.lower())
    if(res=='min'):
        suffix.append('.wdc')
    else:
        suffix.append('')
    for i in range(len(dir_wdc)):
        dir_2=dailynames(trange=trange,file_format='%Y',directory=dir_wdc[i],suffix='/')
        file_names=dailynames(trange=trange,file_format='%y%m',prefix=prefix[i], directory=dir_2[0],suffix=suffix[i])
        local_files=download(remote_file=file_names,remote_path=CONFIG['remote_data_dir_wdc'],last_version=True,local_path=CONFIG['local_data_dir_wdc'])
        out_files.append(local_files)
    out_files = sorted(out_files)
    return out_files
    
