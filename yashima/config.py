import os
CONFIG={'local_data_dir_wdc':'iugonet/wdc_kyoto/geomag/','remote_data_dir_wdc':'http://wdc-data.iugonet.org/data/'}


if os.environ.get('SPEDAS_DATA_DIR') :
    CONFIG['local_data_dir_wdc']=os.sep.join([os.environ['SPEDAS_DATA_DIR'],'iugonet','wdc_kyoto','geomag'])
