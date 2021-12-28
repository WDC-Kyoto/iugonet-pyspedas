

import os

CONFIG = {'local_data_dir': 'iugonet_data/', \
					'remote_data_dir':'http://wdc-data.iugonet.org/'}



if os.environ.get('SPEDAS_DATA_DIR') :
	CONFIG['local_data_dir'] = os.sep.join(\
														 [os.environ['SPEDAS_DATA_DIR'], \
														 'iugonet'])
