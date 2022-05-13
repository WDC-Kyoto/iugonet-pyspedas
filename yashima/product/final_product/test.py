import pyspedas
import pytplot
from pytplot.MPLPlotter.tplot import tplot
import sys
sys.path.append("./iugonet-pysedas/final_product")
import iug_load_gmag_wdc as iug_load_gmag_wdc

iug_load_gmag_wdc.iug_load_gmag_wdc(trange=['2019-1-1', '2019-4-1'],level="final",site="dst kak",res="hour")

tplot("*")
