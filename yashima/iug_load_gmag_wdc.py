from wdc import site as st

def iug_load_gmag_wdc(trange=['2011-1-1', '2011-1-2'],level="final",site="dst kak ae asy",res="hour"):
    site2=site.split(" ")
    if ("dst" in site2):
        from wdc import dst
        dst.dst(trange=trange,level=level)
    if("ae" in site2):
        from wdc import ae
        ae.ae(trange=trange,level=level,res=res)
    if("asy" in site2):
        from wdc import asy
        asy.asy(trange=trange)
    if("sym" in site2):
        from wdc import asm
        sym.sym(trange=trange)
    site2=[s for s in site2 if not((s=="dst")or(s=="ae")or(s=="sym")or(s=="asy"))]
    for ss in site2:
        st.site(trange=trange,res=res,site=ss)
    return 0

def iug_load_gmag_wdc_qddays(trange=['2011-1-1', '2011-1-2']):
    from wdc import gddays
    gddays.qddays(trange=trange)
    return 0

def iug_load_gmag_wdc_wp_index(trange=['2010-1-1', '2010-1-1']):
    from wdc import wp_index
    wp_index.wp_index(trange=trange)
    return 0
