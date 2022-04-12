import os
CONFIG={'local_data_dir_dst':'',
        'local_data_dir_site':'',
        'remote_data_dir_dst':'http://wdc-data.iugonet.org/data/hour/index/',
       'remote_data_dir_site':'http://wdc-data.iugonet.org/data/',}

root_dir=''
if os.environ.get('SPEDAS_DATA_DIR') :
    root_dir = os.environ.get('SPEDAS_DATA_DIR')

CONFIG['local_data_dir_dst']=os.sep.join([root_dir,'iugonet','wdc_kyoto','dst'])
CONFIG['local_data_dir_site']=os.sep.join([root_dir,'iugonet','wdc_kyoto','site'])
