


from load.load_ae_min import load_ae_min
from load.load_ae_hour import load_ae_hour


def ae(trange=['2015-01-01', '2015-01-01'], res='min', level='provisional'):

    ###
    if res == 'min' :
        load_ae_min(trange, level=level)

    if res == 'hour' :
        pass
        load_ae_hour(trange, level=level)


    return True

ae(trange=['2009-12-1', '2010-1-2'])







