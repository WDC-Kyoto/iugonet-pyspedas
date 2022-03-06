


import numpy as np
from pyspedas.utilities.time_double import time_double  
from pyspedas.utilities.time_string import time_string  
from pyspedas.utilities.dailynames  import dailynames  
from pytplot import store_data, options
from pytplot import tplot 
from pytplot import tplot_names 

from .download.download_sym import download_sym 
 


def asy(trange=['2011-1-2', '2011-2-1 11:11:10']) :
	
	### read data
	local_files = download.asy(trange)
	#
	names    = ['h1', 'h2']
	names    = names + ['s' + str(i+1) for i in range(60)] 
	formats0 = ['U', 'U'] 
	formats1 = ['i8'] * 61
	formats  = formats0 + formats1
	dtype    = {'names':names, 'formats': formats}
  #
	asy_d = np.zeros(0, dtype='i8')
	asy_h = np.zeros(0, dtype='i8')


	for lf in local_files:
		buff = np.genfromtxt(lf, dtype=dtype, missing_values='99999', 
		                     filling_values=np.nan, unpack=True)

		l     = len(buff[0])         # (hours of month) x 4
		size  = int( l/4*60 )        # minutes of month, 4:SYM-H, SYM-D, ASY-H, ASY-D  
		asy_d_month = np.zeros(size)
		asy_h_month = np.zeros(size)

		for minute in range(60):
			buff_asy_d  = buff[minute + 2][ [i for i in range(l) if 1  <= (i % 96) < 24] ]
			buff_asy_h  = buff[minute + 2][ [i for i in range(l) if 24 <= (i % 96) < 48] ]  
			#
			asy_d_month[ [i for i in range(size) if i % 60 == minute] ] = buff_asy_d
			asy_h_month[ [i for i in range(size) if i % 60 == minute] ] = buff_asy_h

		asy_d = np.append(asy_d, asy_d_month)
		asy_h = np.append(asy_h, asy_h_month)



  ### convert to tplot variables
  ## time
	fmt   = '%Y-%m-'
	date  = dailynames(trange=trange, file_format=fmt)
  # start time   'YYYY-MM-01'
	t0 = time_double( date[0] + '01' )

  # end time     'YYYY-MM-dd' -> 'YYYY-MM-31'
	days = calendar.monthrange(int(date[1][0:4]), 
	                           int(date[1][5:7]))[1]
	t1   = time_double( date[1] + str(days) + ' 23:59:59' )
  #
	t = np.arange(t0, t1, 60)

	## data
	store_data("ASY-H", data={'x':t, 'y':asy_h}) 
	store_data("ASY-D", data={'x':t, 'y':asy_d}) 


	return 1
 



def ae(trange=['2011-1-2', '2011-2-1 11:11:10']) :
	return 1







 

