
from load.load_dst import load_dst


def dst(trange=['2015-01-01', '2015-01-01'], level='final'):

    load_dst(trange=trange,level=level)

    return True

#dst(trange=['2011-1-1/00:00:00', '2011-1-1/12:00:00'],level='all')
