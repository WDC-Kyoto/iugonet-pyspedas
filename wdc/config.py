

import os

CONFIG = {'local_data_dir_qddays': 'iugonet_data/qddays', 
					'local_data_dir_wp_index':'iugonet_data/wp_index',
					'remote_data_dir_qddays':'http://wdc-data.iugonet.org/',  
					'remote_data_dir_wp_index':'https://www.isee.nagoya-u.ac.jp/~nose.masahito/s-cubed/data/'}



if os.environ.get('SPEDAS_DATA_DIR') :
	CONFIG['local_data_dir_qddays'] = os.sep.join(\
														        [os.environ['SPEDAS_DATA_DIR'], \
														        'iugonet/qddays'])
	CONFIG['local_data_dir_wp_index'] = os.sep.join(\
														         [os.environ['SPEDAS_DATA_DIR'], \
														         'iugonet/wp_index'])
