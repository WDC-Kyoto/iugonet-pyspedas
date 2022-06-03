import pyspedas
import pytplot
from pytplot.MPLPlotter.tplot import tplot
import sys
sys.path.append("./iugonet-pysedas/final_product")
import iug_load_gmag_wdc as iug_load_gmag_wdc

iug_load_gmag_wdc.iug_load_gmag_wdc(trange=['2011-1-1', '2011-2-1'],level="final",site="kak asy sym",res="min")
 
tplot("*")
