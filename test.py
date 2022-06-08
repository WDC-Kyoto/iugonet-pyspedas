import pyspedas
import pytplot
from pytplot.MPLPlotter.tplot import tplot

#sys.pathの変更
#import sys
#sys.path.append("./iugonet-pyspedas/")

import iugonet_wdc.iug_load_gmag_wdc as iug_load_gmag_wdc

#実行部分
iug_load_gmag_wdc.iug_load_gmag_wdc(trange=['2011-1-1', '2011-2-1'],level="final",site="kak asy sym dst ae",res="min")

#spedasのiug_load_gmag_wdcに対応していて
#trange:時間範囲
#levelは'final','provisional','real_time',"all",の4種類
#site:dst,ae,asy,symと各観測点を3文字で表したものをスペース空けて
#res:時間分解能で"hour","min"の２つ

#iug_load_gmag_wdc_qddays(trange=['2011-1-1', '2011-1-2'])
#iug_load_gmag_wdc_wp_index(trange=['2010-1-1', '2010-1-2'])


#tplot変数を描画 
tplot("*")
